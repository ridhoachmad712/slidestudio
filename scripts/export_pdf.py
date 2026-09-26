"""Convert a finalized PPTX to PDF with an existing LibreOffice installation."""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

def find_soffice(explicit):
    if explicit:
        candidate = Path(explicit).expanduser()
        if not candidate.is_file():
            raise FileNotFoundError(f"Executable not found: {candidate}")
        return str(candidate.resolve())
    for name in ("soffice", "libreoffice"):
        candidate = shutil.which(name)
        if candidate:
            return candidate
    candidates = [Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "LibreOffice/program/soffice.com",
                  Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "LibreOffice/program/soffice.exe",
                  Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError("LibreOffice not found. Export PDF in PowerPoint, or pass --soffice PATH.")

def convert(source, out_dir, executable, timeout=120):
    source = source.resolve()
    if not source.is_file() or source.suffix.lower() != ".pptx":
        raise ValueError("Input must be an existing .pptx file")
    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / (source.stem + ".pdf")
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite: {destination}")
    with tempfile.TemporaryDirectory(prefix="lecture-slides-pdf-") as scratch:
        scratch = Path(scratch)
        profile = scratch / "profile"
        output = scratch / "converted"
        output.mkdir()
        command = [executable, f"-env:UserInstallation={profile.as_uri()}", "--headless",
                   "--convert-to", "pdf:impress_pdf_Export", "--outdir", str(output), str(source)]
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
        generated = output / destination.name
        if result.returncode or not generated.is_file():
            raise RuntimeError(f"Conversion failed: {result.stderr or result.stdout}")
        payload = generated.read_bytes()
        if not payload.startswith(b"%PDF-"):
            raise RuntimeError("Converter did not produce a PDF")
        # Exclusive creation also protects against a destination created during conversion.
        with destination.open("xb") as stream:
            stream.write(payload)
    return destination

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--soffice")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    try:
        print(convert(args.pptx, args.out_dir, find_soffice(args.soffice), args.timeout))
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
