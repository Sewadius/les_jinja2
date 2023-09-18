# Filter block with `upper()` example
from jinja2 import Template

persons = [
    {'name': 'Mike', 'old': 18, 'weight': 78.5},
    {'name': 'Nick', 'old': 28, 'weight': 82.3},
    {'name': 'Joe', 'old': 33, 'weight': 94.0}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{ u.name }}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
print(tm.render(users=persons))
