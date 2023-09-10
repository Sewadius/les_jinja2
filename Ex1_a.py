# About the templating engine, the use of {{{}}} in templates
from jinja2 import Template

name = "Федор"
age = 28

tm = Template("Мне {{ a }} лет и зовут {{ n }}.")
msg = tm.render(n=name, a=age)

msg2 = f'Привет {name}'
print(msg, msg2, sep='\n')

tm_2 = Template("Мне {{ a * 2 }} лет и зовут {{ n.upper() }}")
msg3 = tm_2.render(a=age, n=name)

print(msg3)
