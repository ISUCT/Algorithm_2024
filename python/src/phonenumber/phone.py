class Phone:
    def __init__(self, brand_name, color, number):
        self.brand = brand_name
        self.color = color
        self.number = 0
        self.set_number(number)

    def set_number(self, phone_number):
        if 999999999 < phone_number < 10000000000:
            self.number = phone_number
        else:
            raise ValueError("Неправильно набран номер")
        
    def get_number(self):
        return self.number
    
    def set_color(self, phone_color):
        self.color = phone_color

    def get_color(self):
        return self.color
    
    def get_brand(self):
        return self.brand
    
