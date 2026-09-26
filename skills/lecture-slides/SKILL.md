---
name: lecture-slides
description: Create or revise professional university lecture presentations as editable PowerPoint PPTX and PDF files, using academic templates, accurate sources, purposeful visuals, lecturer notes, and rendered slide review. Use for materi kuliah, slide perkuliahan, or academic teaching decks. Does not default to web slides or Bolt Slides.
---

# Lecture Slides

Produce a teaching deck with editable text and evidence in PPTX and, when requested, a PDF distribution copy. Preserve the user's requested format, slide count, references, institutional template, and language. Default to Indonesian for Indonesian requests. Never substitute an HTML/React presentation or a chat outline for a requested PPTX/PDF.

## Brief and template

For a new lecture or a changed audience, depth, or teaching approach, read [needs alignment](references/needs-alignment.md). Resolve content, teaching approach, and visual preferences separately. Extract the brief from ordinary lecturer language and supplied RPS/materials before asking targeted questions. Determine source expansion mode and whether slides accompany a lecture, support independent study, or serve both. Three representative sample slides are optional when style or depth is unclear. Do not impose a new approval gate on a request to finish directly.

Use lecturer profiles as scoped preferences, distinguishing directly stated, provisional, and confirmed entries. Meeting instructions take priority. Do not permanently store inferred or one-deck preferences without authorization. Summarize material assumptions and surface unresolved mandatory conflicts. Plan an outcome coverage map and review against the resolved brief, not only a general visual checklist.

Read the supplied brief, RPS/syllabus, readings, and existing material. Identify student level, prerequisites, observable learning outcomes, duration, total slide count, and required outputs. Ask only about missing information that materially changes the lesson; state reasonable assumptions and continue otherwise.

Use a supplied institutional template first. If the user only supplied a source deck for content, do not assume its design must be copied. In SlideStudio, choose `templates/academic-paper.pptx` for a warm editorial look or `templates/academic-ink.pptx` for a neutral institutional look. These are editable layout libraries, not custom-master POTX files. Preserve their slide dimensions and typography; duplicate layouts according to the content, then replace all sample text and data. Read `docs/DESIGN.md` in the repository for design guidance.

When used outside the kit, follow a provided design reference or choose a restrained 16:9 academic design with clear hierarchy. Do not require the kit files to exist to handle an ordinary deck request.

## Plan the teaching sequence

For depth selection, discipline-specific explanation, or broad revision feedback, read [teaching patterns](references/teaching-patterns.md). Accept a conversational brief and offer concrete examples of depth rather than requiring a long form. Choose an appropriate explanation pattern for each topic, and revise the reasoning or application when asked for more depth rather than merely expanding text.

Create a compact storyboard with each slide's teaching purpose, main point, evidence, visual treatment, and lecturer notes. Sequence concepts from prerequisites to explanations, worked examples, application, and assessment as appropriate. Do not force every lesson into a pitch structure or a fixed number of sections.

- Learning outcomes should specify a demonstrable action: calculate, distinguish, explain a mechanism, or evaluate a case.
- Define notation before using it and preserve the steps students need to follow the reasoning.
- Give one main teaching purpose to each slide. Split dense content when the requested count permits.
- Include examples and comprehension checks that serve the learning outcomes. Do not force numerical exercises into a conceptual subject.
- Put exercise answers, evaluation criteria, lecturer prompts, and likely misconceptions in notes. Use a separate answer slide if students need the answer in the PDF; count it in the requested total.
- End with synthesis and a useful next activity/reading. Avoid sales-style CTAs.

## Accuracy and sources

Use supplied sources first. When research is authorized or needed, verify facts with textbooks, original research, or authoritative institutional sources. Never invent titles, references, page numbers, DOI, quotes, scientific measurements, or real-world datasets.

Label illustrative cases and data as hypothetical. Keep equations, units, assumptions, exceptions, and qualifications that affect the meaning. Resolve source disagreements where possible and flag specific unresolved issues. Cite evidence concisely on the slide and include fuller attribution in notes or a reference slide. A PDF for students must contain the references they need without relying only on notes.

Generated illustrations may explain a concept but do not replace verified anatomy, maps, technical schematics, measured graphs, or other scientific evidence. Preserve source logos and artwork when required and check redistribution rights for shared repositories.

## Editorial and visual quality

Use direct subject titles for definitions and mechanisms; use a supported takeaway when the slide establishes a finding. Avoid slogans, generic “unlocking potential” copy, filler intros, unsupported claims, excessive jargon, repeated conclusions, and decorative subtitles that restate the title.

Use normal academic Indonesian and precise technical terms. Do not force three-item lists or bullets onto every slide. Keep necessary scientific symbols and process arrows when they convey actual meaning. Move extended narration to notes without removing essential assumptions from student-facing content.

Follow the template's fonts, colors, margins, and hierarchy. Otherwise use at most two font families, a neutral background, strong contrast, and one main accent. Use consistent notation and alignment. Shorten or split crowded content before reducing type size. Typical starting sizes are 44–54 pt on a cover, 32–38 pt for titles, 20–26 pt for body text, and 17–20 pt for evidence labels; inspect at the intended presentation size rather than treating these as guarantees.

Choose a visual for its explanatory function: a labeled mechanism diagram, chart with units, concise comparison, worked calculation, case image, or relevant example. Use editable tables/charts and requested diagrams as native slide objects. Avoid repeated card grids, gradient/glow decoration, stock AI imagery, and ornamental 3D scenes. Simple text or an equation can be the strongest composition when it fits the lesson.

## Author and export

Use the presentation tools available in the environment. If the environment supplies a presentation creation skill, read its implementation guidance and use its supported workflow. Do not assume any private library, runtime path, PowerPoint installation, or converter exists on another user's computer. Ordinary lecturers can edit the supplied PPTX templates directly in PowerPoint without a code runtime.

PPTX must contain editable text and native tables/charts where required. Do not make every slide a single screenshot. Keep notes as speaker notes. PDF may be static, but prefer selectable text and crisp graphics. Normally export PDF from the finalized PPTX; do not independently rewrite the lesson into a differently structured PDF. Verify font substitution and mathematical symbols after conversion.

If a requested format cannot be produced, preserve the available editable result, explain the specific missing capability, and give the appropriate manual export step. Do not claim to have created, converted, rendered, or opened a file when that did not happen.

## Inspect before delivery

Render every final slide and inspect it individually. Check text fit, clipping, overlap, line breaks, table/chart labels, formula symbols, citations, alignment, contrast, and consistency with the template. Contact sheets help with overall flow but do not replace full-slide review. Fix issues in the source and re-export.

Check every learning outcome is taught and assessed, examples match the students' level, and slides do not repeat the same explanation. Verify arithmetic, units, exercise answers, references, slide count, and editability. Inspect the PDF too: same count/order/content, readable text, no missing glyphs, and no unintentionally revealed exercise answers.

In the kit, `scripts/check_pptx.py` performs a limited structural check. It cannot certify text fit, design quality, scientific correctness, or application compatibility. Do not introduce unnecessary tests for small reversible edits; do perform the checks relevant to the actual deck.

Deliver the requested files, with concise use instructions and material limitations. Keep validation logs and implementation details out of slides and lecturer notes. Do not publish externally unless authorized.
