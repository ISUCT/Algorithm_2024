class Cat:
    def __init__(self, age, name, color):
        if age >= 19:
            raise ValueError("This age is not correctly specified")    
        self.age = age
        self.name = name
        self.color = color

    def set_age(self, age):
        if age >= 19:
            raise ValueError("This age is not correctly specified")
        else:
            self.age = age

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color