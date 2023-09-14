# Using filter "sum"
from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkswagen', 'price': 21300}
]

tpl = 'Total price of cars {{ cs | sum(attribute="price") }}'
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
