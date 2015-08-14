#!/usr/bin/python3


class Cat:

    def __init__(self, **kwargs):
        self.properties = kwargs

    def meow(self):
        print('Meow..!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

tom = Cat(color='blue', legs=4)
print(tom.get_property('color'))
print(tom.get_properties())

