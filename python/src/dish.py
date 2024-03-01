class Dish:
    def __init__(self, name: str, vid: str, price: int):
        self.__name = name
        self.__vid = vid
        self.check_price(price)
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def vid(self) -> str:
        return self.__vid

    @vid.setter
    def vid(self, value: str):
        self.__vid = value

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, value: int):
        self.check_price(value)
        self.__price = value

    def check_price(self, price: int):
        if price >= 5000 or price <= 0:
            raise ValueError("Это блюдо вам не по карману")

    @property
    def info(self) -> str:
        return f"""Цена: {self.price}
Название: {self.name}
Тип блюда: {self.vid}"""
