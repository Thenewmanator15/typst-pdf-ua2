// Headings inside a block, columns, a grid and padding. Each still opens a section.
#set document(title: "Headings in containers")
#set text(lang: "en")
= At the top
Text.

#block(inset: 6pt)[
  == In a block
  Text in the block.
]

#columns(2)[
  == In columns
  Text in columns.
]

#grid(columns: 2, gutter: 1em)[
  == In a grid cell
  Text in the cell.
][
  == In the next cell
  More text.
]

#pad(left: 1cm)[
  == In padding
  Text in padding.
]

= Back at the top
Text.
