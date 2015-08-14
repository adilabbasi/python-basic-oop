#!/usr/bin/python3

class Animal:
    def talk(self): print('talks like Animal')

    def walk(self): print('Walks like a Aniaml')

    def play(self): print('Walks like a Aniaml')

class Cat(Animal):
    def meow(self):
        print('Meow..!')

    def walk(self):
        super().play()
        print('Walks like a cat.')

class Dog(Animal):
    pass


tom = Cat()
tom.talk()
tom.meow()
tom.walk()

fido = Dog()
fido.walk()

