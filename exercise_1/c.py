# Using substitution on the example of a dictionary
from jinja2 import Template

per = {'name': 'Dave', 'age': 34}

tm = Template('I am {{ per.age }} years old and my name is {{ per.name }}.')
msg = tm.render(per=per)
print(msg)
