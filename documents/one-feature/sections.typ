// Headings at three levels and a bibliography. Each heading opens a section that runs to
// the next heading of the same or a higher level.
#set document(title: "Sections")
#set text(lang: "en")
Text before the first heading.
= One
Text.
== One point one
Text.
=== One point one point one
Text.
== One point two
Text.
= Two
Text @smith2020.

#bibliography("refs.yml", style: "ieee")
