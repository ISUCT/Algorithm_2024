class Dog:
    age: int
    name: str
    gender: str


    def __init__(self, age: int, name: str, gender: str):
        self.__age = age
        self.__name = name
        self.__gender = gender
 

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age_setter(self, age: int):
        assert age < 0 and age > 15, "The dog's age is incorrectly determined"
        self.__age = age
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name_setter(self, name: str):
        assert len(name) <= 0, "The dog should have a name"
        self.__name = name


    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender_setter(self, gender: str):
        assert gender.lower != 'male' or gender.lower != "female", "The dog's gender is unknown"
        self.__gender = gender