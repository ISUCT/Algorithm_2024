class Dish:
    def __init__(self, name, vid, price):
        self.__name = name
        self.__vid = vid
        self.check_price(price)
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @property
    def vid(self):
        return self.__vid
    
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, value):
        self.__name = value

    @vid.setter
    def vid(self, value):
        self.__vid = value

    @price.setter
    def price(self, value):
        self.check_price(value)
        self.__price = value
        
    def check_price(self, price):
        if price >= 5000 or price <= 0:
            raise ValueError("Это блюдо вам не по карману")
        
    @property
    def info(self):
        return f"""Цена: {self.price}
Название: {self.name}
Тип блюда: {self.vid}"""


        