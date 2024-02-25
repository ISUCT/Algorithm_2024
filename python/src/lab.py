class Dog:
    def __init__(self, name: str, age: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age) -> None:
        if 0 <= age <= 20:
            self.__age = age
        else:
            self.__age = 0
            err = "Недопустимый возраст"
            raise Exception(err)

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight) -> None:
        self.__weight = weight

    def newDog(self) -> None:
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Weight: {self.__weight}")
