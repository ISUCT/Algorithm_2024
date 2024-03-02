class Person:
    def __init__(self, age, name, gender):
        self.age = 0
        self.set_age(age)
        self.name = name
        self.gender = gender

    def set_age(self, age):
        if age < 0 or age > 130:
            raise 'Возраст не соответствует условиям'
        else:
            self.age = age

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def death_person(self):
        if self.gender == 'муж':
            print(f'{self.name} был найден убитым')
        elif self.gender == 'жен':
            print(f'{self.name} была найдена убитой')
        else:
            print(f'{self.name} было найдено убитым')
# try:
#     p = Person(1, 'jdfghk', 1)
# except ArithmeticError:
#     print('Не в мою смену')