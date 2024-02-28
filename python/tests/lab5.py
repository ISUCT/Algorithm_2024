class Cat():

    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.Rules()

    def Rules(self):
        if not isinstance(self.name, str):
            raise TypeError("Неверный тип данных name")
        if self.age < 0 or self.age > 15:
            raise ValueError("Неверно указан возраст")
        elif self.height < 0 or self.height > 25:
            raise ValueError("Неверно указан рост")
        elif self.weight < 0 or self.weight > 8:
            raise ValueError("Неверно указан вес")
        print(f"Успешное создание\nИмя кошки: {self.name}\nВозраст: {self.age} лет\nВес: {self.weight} кг\nРост: {self.height} см ")
        