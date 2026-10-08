"""make_doc.py CHAPTERS OUT: writes a large Typst document that uses what the PDF/UA-2
prototype touches: an outline, numbered headings with labels, cross-references,
footnotes, citations, figures with captions (a table and a described shape), equations
with alternative text, lists and a block quote."""
import sys

chapters = int(sys.argv[1])
out = [
    '#set document(title: "Benchmark")',
    '#set text(lang: "en")',
    '#set heading(numbering: "1.1")',
    '#outline()',
    '',
]
for c in range(chapters):
    other = (c * 7 + 3) % chapters
    out.append(f'= Chapter {c + 1} <ch-{c}>')
    for s in range(3):
        out.append(f'== Section {c + 1}.{s + 1} <sec-{c}-{s}>')
        for p in range(4):
            out.append(
                f'#lorem(70) See @ch-{other} and @sec-{other}-{(s + p) % 3}.'
                f'#footnote[A note in chapter {c + 1}. #lorem(12)] As shown in @ref:jCAS09.'
            )
            out.append('')
    out.append(
        f'#figure(table(columns: 3, table.header[A][B][C], [1], [2], [3], [4], [5], [6]),'
        f' caption: [A table in chapter {c + 1}.]) <tab-{c}>'
    )
    out.append(
        f'#figure(rect(width: 3cm, height: 1.5cm, fill: aqua), alt: "A shaded box",'
        f' caption: [A box in chapter {c + 1}.]) <fig-{c}>'
    )
    out.append(f'See @tab-{c} and @fig-{c}.')
    out.append('#math.equation(block: true, alt: "a squared plus b squared equals c squared", $ a^2 + b^2 = c^2 $)')
    out.append('- one\n- two\n+ first\n+ second')
    out.append('#quote(block: true)[A quoted _sentence_ here.]')
    out.append('')
out.append('#bibliography("references.yml", style: "ieee")')
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
