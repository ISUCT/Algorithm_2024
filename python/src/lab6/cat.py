class Cat():
    __age = 0
    __name = ""
    __breed = ""

    def __init__(self, age, name, breed):
        self.age = age
        self.__name = name
        self.__breed = breed

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age):
        assert (age >= 0 and age <= 25), "Invalid age"
        self.__age = age

    @property
    def breed(self) -> str:
        return self.__breed
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def petTheCat(self):
        print("Cat {0} says meow\n".format(self.__name))