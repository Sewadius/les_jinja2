# About the templating engine, the use of {{{}}} in templates
from jinja2 import Template

name = "Nick"
age = 28

tm = Template("I am {{ a }} years old and my name is {{ n }}.")
msg = tm.render(n=name, a=age)

msg2 = f'Hi, {name}'
print(msg, msg2, sep='\n')

tm_2 = Template("I am {{ a * 2 }} years old and my name is {{ n.upper() }}.")
msg3 = tm_2.render(a=age, n=name)

print(msg3)
