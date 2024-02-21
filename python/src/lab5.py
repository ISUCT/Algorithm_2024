class Car: 
    def __init__(self, speed, color, size, distance):
        self.speed = speed
        self.color = color
        self.size = size
        self.distance = distance
         
    def set_speed(self, speed):
        if 0 < speed < 300:
            self.speed = speed
        else:
            print("Максимальная скорость должна быть не меньше 0 и больше 300")
        
    def get_speed(self):
        return self.speed
    
    def set_color(self, color):
        self.color = color 

    def get_color(self):
        return self.color

    def get_distance(self):
        return self.distance
    
    def set_distance(self, distance):
        if distance > 0:
            self.distance = distance
        else:
            print(" Расстояние должно быть не меньше 0")
    
    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size 
