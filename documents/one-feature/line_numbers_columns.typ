// Numbered lines over two columns and two pages, with bold text that runs over a line
// end, a footnote and a list. Each number has to end up at its own line in the tag tree.
#set document(title: "Line numbers in columns")
#set text(lang: "en")
#set page(width: 14cm, height: 9cm, margin: (x: 2cm), columns: 2)
#set par.line(numbering: "1")
= A heading
#lorem(60) Some *bold text that wraps over a line end* and a footnote.#footnote[A note.]

#lorem(80)

- A list item that is long enough to wrap onto a second line in this column.
- Another.
