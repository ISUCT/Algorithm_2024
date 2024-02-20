class Car:
    def __init__(self, model, maxspeed, price, mileage):
        self.model = model
        self.maxspeed = maxspeed
        self.price = price
        self.mileage = mileage

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_maxspeed(self, maxspeed):
        if 0 < maxspeed < 420:
            self.maxspeed = maxspeed
        else:
            print("Максимальная скорость должна быть больше 0 и меньше 420")

    def get_maxspeed(self):
        return self.maxspeed

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_mileage(self, mileage):
        self.price = mileage

    def get_mileage(self):
        return self.mileage

    def print_car(self):
        print("Модель:", self.model, "Макс. скорость:", self.maxspeed,
              "Цена:", self.price, "Пробег:", self.mileage)