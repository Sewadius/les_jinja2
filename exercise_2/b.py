# HTML code shielding
from jinja2 import Template
from markupsafe import escape

link = '''In HTML document links are defined as:
<a href="#">Ссылка</a>'''

tm = Template("{{ link }}")
print(tm.render(link=link), end='\n\n')

tm_2 = Template("{{ link | e }}")
print(tm_2.render(link=link), end='\n\n')

# Using "escape"
msg = escape(link)
print(msg)