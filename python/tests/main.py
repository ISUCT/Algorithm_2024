class ACE:
    def __init__(self, firepower, speed, armor, name):
        self.firepower = firepower
        self.speed = speed
        self.armor = armor
        self.name = name
        
        if self.set_firepower(firepower) is None:
            raise ValueError("неверно указана огневая мощь, пожалуйста, измените параметр")
        if self.set_speed(speed) is None:
            raise ValueError("неверно указана скорость, пожалуйста, измените параметр")
        if self.set_armor(armor) is None:
            raise ValueError("неверно указано бронирование, пожалуйста, измените параметр")
        
    def GIVEMEBACK(self):
        print(f"Ваш Ace создан.\nИмя Ace: {self.name}\nОгневая мощь: {self.firepower}\nСкорость: {self.speed}\nБроня: {self.armor}\n")

    
    def get_firepower(self):
        return self.firepower
    
    def set_firepower(self, firepower):
        if firepower <= 0 or firepower > 5000:
            return None
        else:
            return firepower
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        if speed <= 0 or speed > 5000:
            return None
        else:
            return speed
    
    def get_armor(self):
        return self.armor
    
    def set_armor(self, armor):
        if armor <= 0 or armor > 5000:
            return None
        else:
            return armor 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

ace1 = ACE(5000 , 1000, 1000, "Steel Haze")
ace1.GIVEMEBACK()
