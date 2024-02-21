class Cat:
    name: str = ""
    age: int = 0
    sex: str = ""

    def __init__(self, name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def PrintAllProperty(self):
        print("Имя кошки:", self.name)
        print("Возраст кошки:", self.age)
        print("Пол кошки:",self.sex)

    def setAge(self, newAgeValue):
        if 0 <= newAgeValue <= 30:
            self.age = newAgeValue
        else:
            print("Incorrect age")
            self.age = 0

    def getAge(self):
        return self.age