class Mouse():
    name = None
    age = None
    color = None
    gender = None

    def __init__(self, name: str, age: int, color: str, gender: str):
        self.Check(name, age, color, gender)
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def Check(self, name: str, age: int, color: str, gender: str ):
        if not name.isalpha():
            raise TypeError("Ошибка, неверный тип данных для параметра name. Ожидается строка.")
        elif age < 0 or age > 5:
            raise ValueError("Ошибка, неверно указано значение возраста")
        elif not color.isalpha():
            raise TypeError("Ошибка, неверный тип данных для параметра color. Ожидается строка.")
        elif not gender.isalpha():
            raise TypeError("Ошибка, неверный тип данных для параметра gender. Ожидается строка.")
    def get(self):
        if self.age == None or self.gender == None or self.color == None or self.age == None:
            print("Есть неуказанные значения в параметрах человека: None, попробуйте пересоздать Мыша!")
        else:
            print(f"Мышонок создан.\nИмя мыша: {self.name}\nВозраст: {self.age} лет\nПол: {self.gender} \nЦвет: {self.color}  ")