class Dish:
    def __init__(self, price, calorie, name):
        self.set_price(price)
        self.set_calorie(calorie)
        self.set_name(name)
    def set_price(self, price):
        if price < 0 or price > 1000:
            raise ValueError(f"Dish with cost {price} doesnt exist")
        else:
            self._price = price
    def set_calorie(self, calorie):
        if calorie < 0:
            raise ValueError(f"Dish with calory {calorie} doesnt exist")
        else:
            self._calorie = calorie
    def set_name(self, name):
        self._name = name
    def get_price(self, price):
        return self._price
    def get_calorie(self, calorie):
        return self._calorie
    def get_name(self, name):
        return self._name
    def print_bludo(self):
        print("cost is", self._price, "\n" "calory is", self._calorie, "\n" "name is", self._name)
    
