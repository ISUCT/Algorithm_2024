class Game_Character():

    def __init__(self, nickname: str, level: int, rang: str):
        self.rang = rang
        self.level = level
        self.nickname = nickname
        self.Rules()

    def Rules(self):
        if not isinstance(self.nickname, str):
            raise TypeError("Неверный тип данных name")
        if self.level < 0:
            raise ValueError("Выйди и удали игру")
        print(f"Успешное создание персонажа!\nНик: {self.nickname}\nУровень: {self.level}\nРанг: {self.rang}")