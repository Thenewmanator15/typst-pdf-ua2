# PDF/UA-2 from Typst: a working prototype

The page is at https://thenewmanator15.github.io/typst-pdf-ua2/.

An experiment to see what Typst and krilla need in order to export PDF/UA-2, checked with
veraPDF. The code was written with Claude, an AI assistant. It has not been reviewed by
anyone who knows the PDF specification well, and it is not offered to Typst as a pull
request, since Typst does not accept AI-written code.

- `index.html`: the page.
- `pdf/`: the same documents exported by Typst today and by the prototype.
- `documents/`: the demo, 23 one-feature documents, a test of the thesis template's heading
  levels, and the generator for the 373-page document.
- `tools/`: `check.sh` compiles and validates the documents, `bench.py` times two builds,
  `structdump.py` prints where a tag sits in a PDF's structure tree, and `svgpos.py`
  compares where everything is drawn on the pages of two builds.
- `results/summary.txt`: the numbers.

The code itself is on two branches:

- Typst: https://github.com/Thenewmanator15/typst/tree/ua2-prototype
- krilla: https://github.com/Thenewmanator15/krilla/tree/ua2-structure-destinations,
  discussed in https://github.com/LaurenzV/krilla/issues/449

The thesis sample in `pdf/` is built from
[casson-uom-thesis](https://github.com/ALEX-CASSON-LAB/casson-uom-thesis) by Alex Casson
(MIT No Attribution). `documents/large/references.yml` is from the same template.
