"""Read-only structural checks for lecture decks. Python standard library only."""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from posixpath import normpath, join

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
def relationships(archive, part):
    base, name = part.rsplit("/", 1)
    relpath = f"{base}/_rels/{name}.rels"
    if relpath not in archive.namelist():
        return {}
    result = {}
    for rel in ET.fromstring(archive.read(relpath)):
        if rel.get("TargetMode") == "External":
            continue
        target = rel.get("Target", "")
        result[rel.get("Id")] = (rel.get("Type", ""),
            target.lstrip("/") if target.startswith("/") else normpath(join(base, target)))
    return result

def inspect(path, expected=None, require_notes=False, allow_placeholders=False):
    errors, warnings, slides = [], [], []
    with zipfile.ZipFile(path) as archive:
        members = set(archive.namelist())
        bad = archive.testzip()
        if bad:
            errors.append(f"Corrupt ZIP member: {bad}")
        for relpath in members:
            if not relpath.endswith('.rels'):
                continue
            base = '' if relpath == '_rels/.rels' else relpath.rsplit('/_rels/', 1)[0]
            for rel in ET.fromstring(archive.read(relpath)):
                if rel.get('TargetMode') == 'External':
                    continue
                target = rel.get('Target', '')
                resolved = target.lstrip('/') if target.startswith('/') else normpath(join(base, target))
                if resolved not in members:
                    errors.append(f"Missing relationship target: {resolved}")
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        size = presentation.find("p:sldSz", NS)
        width, height = int(size.get("cx")), int(size.get("cy"))
        refs = relationships(archive, "ppt/presentation.xml")
        ids = presentation.findall("p:sldIdLst/p:sldId", NS)
        if expected is not None and len(ids) != expected:
            errors.append(f"Expected {expected} slides; found {len(ids)}")
        for number, item in enumerate(ids, 1):
            rid = item.get(f"{{{NS['r']}}}id")
            if rid not in refs:
                errors.append(f"Slide {number}: missing relationship")
                continue
            part = refs[rid][1]
            root = ET.fromstring(archive.read(part))
            text = " ".join(t.text or "" for t in root.findall(".//a:t", NS))
            rels = relationships(archive, part)
            notes_parts = [target for typ, target in rels.values() if typ.endswith("/notesSlide")]
            notes_text = ""
            for target in notes_parts:
                note_root = ET.fromstring(archive.read(target))
                # Exclude auto-generated slide number/header/footer placeholders.
                for shape in note_root.findall(".//p:sp", NS):
                    placeholder = shape.find("p:nvSpPr/p:nvPr/p:ph", NS)
                    if placeholder is not None and placeholder.get("type") in {"sldNum", "hdr", "ftr", "dt", "sldImg"}:
                        continue
                    notes_text += " ".join(t.text or "" for t in shape.findall(".//a:t", NS))
            if not text.strip():
                warnings.append(f"Slide {number}: no editable text detected (may be intentional)")
            if require_notes and not notes_text.strip():
                errors.append(f"Slide {number}: no lecturer notes")
            if not allow_placeholders and re.search(r"\blorem ipsum\b|\bTODO\b|\[masukkan[^\]]*\]|\[nama dosen\]|\bJudul pertemuan\b|\bNama mata kuliah\b", text, re.I):
                errors.append(f"Slide {number}: unresolved sample/placeholder text")
            tree = root.find("p:cSld/p:spTree", NS)
            for obj in list(tree) if tree is not None else []:
                if obj.tag == f"{{{NS['p']}}}grpSp":
                    warnings.append(f"Slide {number}: grouped object geometry not checked")
                    continue
                transform = obj.find("p:spPr/a:xfrm", NS)
                if transform is None:
                    transform = obj.find("p:xfrm", NS)
                if transform is None:
                    continue
                offset, extent = transform.find("a:off", NS), transform.find("a:ext", NS)
                if offset is None or extent is None:
                    continue
                x, y, w, h = (int(offset.get("x")), int(offset.get("y")), int(extent.get("cx")), int(extent.get("cy")))
                if x < -9525 or y < -9525 or x + w > width + 9525 or y + h > height + 9525:
                    warnings.append(f"Slide {number}: object extends outside canvas")
            chart_count = sum(typ.endswith("/chart") for typ, _ in rels.values())
            table_count = len(root.findall(".//a:tbl", NS))
            slides.append({"number": number, "editable_text": bool(text.strip()),
                           "notes": bool(notes_text.strip()), "charts": chart_count, "tables": table_count})
    return {"file": str(path), "slides": slides, "errors": errors, "warnings": warnings,
            "scope": "Structural checks only. Render review and academic verification still required."}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--slides", type=int)
    parser.add_argument("--require-notes", action="store_true")
    parser.add_argument("--allow-placeholders", action="store_true", help="Use only on template libraries")
    args = parser.parse_args()
    try:
        result = inspect(args.pptx, args.slides, args.require_notes, args.allow_placeholders)
    except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError, ValueError, AttributeError) as exc:
        print(f"Cannot inspect PPTX: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0

if __name__ == "__main__":
    sys.exit(main())
