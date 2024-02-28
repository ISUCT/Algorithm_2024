class Bunny:
    def __init__(self, name: str, age: int, weight: int) -> None:
        self.age = age
        self.name = name
        self.__weight = weight

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if age >= 0 and age <= 10:
            self.__age = age
        else:
            self.__age = 0
            err = 'Введён неправильный возраст'
            raise Exception(err)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight) -> None:
        if weight >= 62 and weight <= 6000:
            self.__weight = weight
        else:
            err = 'Введён неправильный вес'
            raise Exception(err)

    def display_info(self) -> None:
        print(f"Имя кролика: {self.__name}")
        print(f"Возраст кролика: {self.__age}")
        print(f"Вес кролика: {self.__weight}")
