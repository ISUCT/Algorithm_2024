class Mouse: 
    def __init__(self, age, color, name, gender): 
        self.age = age 
        self.color = color 
        self.name = name 
        self.gender = gender 
 
    def get_age(self): 
        return self.age 
     
    def set_color(self, color): 
        self.color = color 
 
    def get_color(self): 
        return self.color 
     
    def set_age(self, age): 
        if 0 < age < 3: 
            self.age = age  
        else: 
            print("Максимальный возраст должен быть больше 0 и меньше 3") 
 
    def set_name (self, name): 
        self.name = name  
 
    def get_name(self): 
        return self.name 
     
    def set_gender(self, gender): 
        self.gender = gender 
 
    def get_gender(self): 
        return self.gender 
     
    def print_mouse(self): 
        print("Возраст:", self.age, "Цвет:", self.color, 
              "Имя:", self.name, "Пол:", self.gender) 