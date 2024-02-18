class Employee:
    def __init__(self, name: str, age: int, date: str):
        self.__name = name
        self.set_age(age)
        self.__date = date

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_age(self):
        return self.age

    def set_age(self, age):
        if 17 < age < 70:
            self.age = age
        else:
            return "Age is incorrect"

    def print_employee(self):
        return f"Name: {self.__name}\t Age: {self.age}\t Date: {self.__date}"