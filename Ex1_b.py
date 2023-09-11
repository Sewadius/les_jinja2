# Using substitution on the example of classes
from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person = Person('Mike', 33)

tm = Template('I am {{ p.age }} years old and my name is {{ p.name }}.')
tm_2 = Template('I am {{ p.get_age() }} years old and my name is {{ p.get_name() }}')

msg = tm.render(p=person)
msg2 = tm_2.render(p=person)

print(msg, msg2, sep='\n')
