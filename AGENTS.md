# SlideStudio

For new lectures, read `skills/lecture-slides/references/needs-alignment.md`. Read an available `course/lecturer-profile.md` as scoped preferences. Resolve source expansion, slide function, depth, and meeting requirements; use `course/coverage-map.md` to connect outcomes with teaching and assessment. Do not impose sample-slide approval when the lecturer requests completion directly. Do not persist provisional preferences without authorization.

This repository produces editable PPTX lecture decks and PDF distribution copies. Read `skills/lecture-slides/SKILL.md` before creating or revising a deck. Read `course/brief.md` and explicitly provided source materials. Use the requested institutional template first; otherwise choose a supplied layout library according to the brief.

The deliverable is a file, not a React app, HTML presentation, or a chat outline. Use a presentation tool available in the current environment. Preserve editable text, tables, charts, and requested diagrams. Do not flatten a whole slide into an image to obtain a PPTX.

Plan the learning sequence and verify sources before polishing layouts. Render all final slides and inspect them individually. PDF should come from the same final content, normally an export of the finalized PPTX. Report missing tools and unavailable checks accurately. Do not deploy, publish, or upload course materials externally unless authorized.

Store scratch work in `work/` and final lecture files in `outputs/`. The structural checker in `scripts/check_pptx.py` supports quality control but cannot certify appearance or academic correctness. It permits intentional template text with `--allow-placeholders`; do not use that option on completed lecture decks to hide unresolved content.
