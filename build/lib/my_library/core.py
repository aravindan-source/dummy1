# core.py
def greet(name):
    return f"Hello, {name}!"

class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def greetme(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."