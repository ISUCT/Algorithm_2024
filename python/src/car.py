class Car:
    def __init__(self, speed, weight, name):
        self._speed = speed
        self.check_speed(speed)
        self._weight = weight
        self.check_weight(weight)
        self._name = name

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, skorost):
        self.check_speed(skorost)
        self._speed = skorost

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, ves):
        self.check_weight(ves)
        self._weight = ves

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, imya):
        self._name = imya

    @name.setter
    def name(self, imya):
        self._name = imya

    def check_speed(self, speed):
        if speed >= 500 or speed <= 0:
            raise ValueError("Чет не так со скоростью")

    def check_weight(self, weight):
        if weight >= 2000 or weight <= 1000:
            raise ValueError("Чет не так с весом")

    @property
    def mashina(self):
        return f"""Скорость: {self.speed}
Вес: {self.weight}
Марка машины: {self.name}"""
