+++
widget = "portfolio"
headless = true
title = "IBDGC Funded Projects"

[content]
page_type = "project"
filter_default = 0

  [[content.filter_button]]
  name = "All"
  tag = "*"

  [[content.filter_button]]
  name = "Current"
  tag = "Current"

  [[content.filter_button]]
  name = "R01"
  tag = "R01"

  [[content.filter_button]]
  name = "R21"
  tag = "R21"

[design]
columns = "2"
view = 2
flip_alt_rows = false

[design.spacing]
  padding = [ "", "", "", "50px" ]

+++
