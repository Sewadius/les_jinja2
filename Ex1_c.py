# Using substitution on the example of a dictionary
from jinja2 import Template

per = {'name': 'Федор', 'age': 34}

tm = Template('Мне {{ per.age }} лет и зовут {{ per.name }}.')
msg = tm.render(per=per)
print(msg)
