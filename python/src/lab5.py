class Airplane:
    def __init__(self, model, speed, manufcountry):
        self._model = model
        self.set_speed(speed)
        self._speed = speed
        self._manufcountry = manufcountry

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_speed(self, speed):
        if speed > 0 and speed < 10000:
            self._speed = speed
        else:
            raise Exception("Failed set_speed() for airplane model", speed, "is invalid number")

    def get_speed(self):
        return self._speed

    def set_manufcountry(self, manufcountry):
        self._manufcountry = manufcountry

    def get_manufcountry(self):
        return self._manufcountry

    def print_airplane(self):
        print("Модель:", self._model, "\n"
              "Скорость:", self._speed, "\n"
              "Страна производитель:", self._manufcountry)