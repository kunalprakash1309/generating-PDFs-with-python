import sys
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML, CSS

if len(sys.argv) != 3:
    sys.exit("Usage: python render50.py INPUT OUTPUT")

input = sys.argv[1]
output = sys.argv[2]

with open(input, "r") as file:
    lines = file.read()

markup = "<!DOCTYPE>\n"
markup += "<markup>\n"
markup += "<head>\n"
markup += "<style>\n"
markup += "</style>\n"
markup += "</head>\n"
markup += "<body>\n"
markup += highlight(lines, CLexer(), HtmlFormatter())
markup += "</body>\n"
markup += "</html>\n"

properties = "@page { margin: .5in; size: letter landscape;}"
properties += "pre { font-size: 10pt; overflow-wrap: break-word; white-space: pre-wrap};"

css1 = CSS(string=properties)
css2 = CSS(string=HtmlFormatter().get_style_defs(".highlight"))

html = HTML(string=markup)
html.write_pdf(output, stylesheets=[css1, css2])

print("Done")