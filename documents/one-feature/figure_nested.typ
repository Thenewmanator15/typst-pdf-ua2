// Figures with captions in places other than directly in the document: a list item, a
// table cell, a block quote, a section with a heading, and one that holds code.
#set document(title: "Nested figures")
#set text(lang: "en")

= A section

- An item with a figure:
  #figure(rect(width: 2cm, height: 1cm, fill: aqua), alt: "A box", caption: [In a list.])

#table(
  columns: 2,
  table.header[What][Figure],
  [A cell], figure(rect(width: 2cm, height: 1cm, fill: aqua), alt: "A box", caption: [In a cell.]),
)

#quote(block: true)[
  #figure(rect(width: 2cm, height: 1cm, fill: aqua), alt: "A box", caption: [In a quote.])
]

#figure(
  ```rust
  fn main() {}
  ```,
  caption: [A listing.],
)

#figure(
  [Some text and #box(rect(width: 1cm, height: 0.5cm, fill: aqua)) a shape.],
  caption: [Mixed content.],
)
