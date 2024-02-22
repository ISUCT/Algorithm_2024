class Dog:
    def __init__(self, age, ves, poroda):
        self.age = age
        self.ves = ves
        self.poroda = poroda

    def set_age(self, age):
        if 0 <= age <= 20:
            self.age = age
        else:
            raise ValueError("неправильный возраст")

    def set_ves(self, ves):
        if 5 <= ves <= 65:
            self.ves = ves
        else:
            raise ValueError("неправильный вес")

    def set_poroda(self, poroda):
        self.poroda = poroda

    def get_age(self):
        return self.age

    def get_ves(self):
        return self.ves

    def get_poroda(self):
        return self.poroda


def new_dog(age, ves, poroda):
    dog = Dog(age, ves, poroda)
    return dog
