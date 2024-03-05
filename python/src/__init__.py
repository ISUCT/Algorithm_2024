class Cat:
    def __init__ (self, name: str, age: int, breed: str):
        self.__name = name
        self.__age = age
        self.__breed = breed
        self.check_age(age)

    def check_age(self, age:int):
        if age < 0 or age > 18:
            print(f"Вы указали не верный возраст вашего питомца!")
        else:
            self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n: str):
        self.__name = n

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, a: int):
        self.check_age(a)
        self.__age = a

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, b: str):
        self.__breed = b

    def output(self):
        print(f"Имя вашего питомца - {self.__name}")
        print(f"Возраст вашего питомца - {self.__age}")
        print(f"Порода вашего питомца - {self.__breed}")

