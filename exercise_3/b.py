# Using filter "max" to show the row with maximum price
from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkswagen', 'price': 21300}
]

# Dictionary as a result
tpl = 'Row with maximum price: {{ cs | max(attribute="price") }}'
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

# Outputs only car model
tpl = 'Model car with maximum price: {{ (cs | max(attribute="price")).model }}'
tm = Template(tpl)
print(tm.render(cs=cars))
