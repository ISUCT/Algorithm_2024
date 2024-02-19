class Rabbit:
    def __init__(self, name: str, weight: int, age: int):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not isinstance(weight, int):
            raise TypeError("weight must be int")

        self.__name = name
        self.__weight = weight
        self.age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError("age must be int")
        if age < 0 or age > 10:
            raise ValueError(age)
        self.__age = age

    def __str__(self) -> str:
        return (f"rabbit's name is: {self.__name}, "
                f"rabbit's weight is: {self.__weight}, "
                f"rabbit's age is: {self.__age}")
