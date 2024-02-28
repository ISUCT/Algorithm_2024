class Person():
    name = None
    age = None
    weight = None
    height = None
    
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.Proverka(name, age, weight, height)
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def Proverka(self, name: str, age: int, weight: float, height: float ):
        #Проверка типов данных
        if not isinstance(name, str):
            raise TypeError("Ошибка, неверный тип данных для параметра name. Ожидается строка.")
        if not isinstance(age, int):
            raise TypeError("Ошибка, неверный тип данных для параметра age. Ожидается целое число.")
        if not isinstance(weight, float):
            raise TypeError("Ошибка, неверный тип данных для параметра weight. Ожидается действительное число.")
        if not isinstance(height, float):
            raise TypeError("Ошибка, неверный тип данных для параметра height. Ожидается число с плавающей точкой.")
        #Проверка интервалов
        if age < 0 or age > 200:
            raise ValueError("Ошибка, неверно указано значение возраста")
        elif height < 0 or height > 500:
            raise ValueError("Ошибка, неверно указано значение роста")
        elif weight < 0 or weight > 1000:
            raise ValueError("Ошибка, неверно указано значение веса")
        
    def get(self):
        if self.age == None or self.weight == None or self.height == None or self.age == None:
            print("Есть неуказанные значения в параметрах человека: None, попробуйте пересоздать человека!")
        else:
            print(f"Человек создан.\nИмя человека: {self.name}\nВозраст: {self.age} лет\nВес: {self.weight} кг\nРост: {self.height} м ")