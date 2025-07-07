class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."