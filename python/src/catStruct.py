class Cat():
    __age = 0
    __gender = ""
    __breed = ""
    name = ""
    def __init__(self, age: int, gender: str, breed: str, name: str):
            self.__age = age
            self.__gender = gender
            self.__breed = breed
            self.name = name
        
        
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name: str):
        self.name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        if age >= 17:
            raise ValueError(f"I think, there is'not cat, because his age is {age}")
        else:
            self.__age = age
    @property
    def breed(self):
        return self.__breed
    @breed.setter
    def name(self,breed: str):
        self.__breed = breed
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def name(self,gender: str):
        self.__gender = gender