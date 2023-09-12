# Using if in for cycle in the dictionary
from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Moscow'},
    {'id': 5, 'city': 'Paris'},
    {'id': 7, 'city': 'New York'},
    {'id': 8, 'city': 'Saint-Petersburg'},
    {'id': 11, 'city': 'London'},
]

# "-%" is used to skip empty lines
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{ c['id'] }}>{{ c['city'] }}"</option>
{% elif c.city == 'Moscow' -%}
    <option>{{ c['city'] }}</option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
