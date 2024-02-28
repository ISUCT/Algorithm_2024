class Cat:

    def __init__(self, age, breed, name):
        self.name = name
        self.age = 0
        self.breed = breed
        self.set_age(age)

    def set_age(self, new_age):
        if new_age < 0:
            print("Возраст не может быть меньше 0")
        else:
            self.age = new_age

    def set_breed(self, new_breed):
        self.breed = new_breed

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def print_info_cat(self):
        print("------------------------------", "\nCat's name is", self.get_name(), "\nCat's breed is", self.get_breed(), "\nCat's age is", self.get_age())
