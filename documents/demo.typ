// A short document with the things PDF/UA-2 is particular about: a contents list,
// headings, a cross-reference, a footnote, a figure with a caption, a table, a described
// equation, a block quote and a list.
#set document(title: "A small PDF/UA-2 demonstration")
#set text(lang: "en")
#set heading(numbering: "1.1")

#title()

#outline()

= Introduction <intro>
This document is small on purpose. It has one of each thing that a tagged PDF has to
describe carefully, so that the tags can be read by eye.#footnote[A footnote. Its number
in the text and the note itself have to point at each other.]

A link inside the document, to @method, and one outside it, to
#link("https://pdfa.org")[the PDF Association].

= Method <method>
See @fig:box for a figure and @tab:values for a table.

#figure(
  rect(width: 4cm, height: 2cm, fill: aqua),
  alt: "A plain shaded rectangle",
  caption: [A figure with an alternative description.],
) <fig:box>

#figure(
  table(
    columns: 3,
    table.header[Quantity][Value][Unit],
    [Length], [4], [cm],
    [Height], [2], [cm],
  ),
  caption: [A table with a header row.],
) <tab:values>

#math.equation(
  block: true,
  alt: "a squared plus b squared equals c squared",
  $ a^2 + b^2 = c^2 $,
)

#quote(block: true)[A block quote with some _emphasis_ in it.]

+ A first numbered item
+ A second numbered item
