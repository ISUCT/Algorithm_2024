class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def describe(self):
        return f"{self.name} - это {self.age} - летняя собака породы {self.breed}."
