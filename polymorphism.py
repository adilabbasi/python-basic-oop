#!/usr/bin/python3

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('tom'),
           Dog('Lassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())

