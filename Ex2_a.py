# Using `raw` to ignore substitution
from jinja2 import Template

data = '''{% raw %}The Jinja module
instead of {{ name }} definition
substitutes corresponding value{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Mike')
print(msg)
