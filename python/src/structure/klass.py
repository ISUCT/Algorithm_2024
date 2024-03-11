class ship:
    def __init__(self, name: str, length: float, displacement: float, max_speed_knots: float):
        self.__name = name 
        self.__length = length
        self.__displacement = displacement
        self.__max_speed_knots = max_speed_knots
        self.check_length(length, name)
        self.check_displacement(displacement, name)
        self.check_max_speed(max_speed_knots, name)


    def check_length(self,  length: float, name: str):
        if length < 0:
            print(f"Длина {name} указана не верно, т.к. не может быть отрицательной!")
            self.__length = -length
        else:
            self.__length = length

    def check_displacement(self, displacement: float, name: str):
        if displacement < 0:
            print(f"Объём {name} указан неверно, т.к. не может быть отрицательным!")
            self.__displacement = -displacement
        else:
            self.__displacement = displacement

    def check_max_speed(self, max_speed_knots: float, name: str):
        if max_speed_knots < 0:
            print(f"Максимальная скорость {name} указана не верно, т.к. не может быть отрицательной!")
            self.__max_speed_knots = -max_speed_knots
        else:
            self.__max_speed_knots = max_speed_knots

    def Sail(self):
        print(f"{self.__name} sails!")


    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    @property
    def displacement(self):
        return self.__displacement

    @property
    def max_speed_knots(self):
        return self.__max_speed_knots

    @name.setter
    def name(self, name):
        self.__name = name
    
    @length.setter
    def length(self, length: float):
        if length < 0:
            print("Длина не может быть отрицательной!")
            self.__length = -length
        else:
            self.__length = length
    
    @displacement.setter
    def displacement(self, displacement: float):
        if displacement < 0:
            print("Объём не может быть отрицательным!")
            self.__displacement = -displacement
        else:
            self.__displacement = displacement
        
    @max_speed_knots.setter
    def max_speed_knots(self, max_speed_knots: float):
        if max_speed_knots < 0:
            print("Максимальная скорость не может быть отрицательной!")
            self.__max_speed_knots = -max_speed_knots
        else:
            self.__max_speed_knots = max_speed_knots

    def output(self):
        print(f"Длина {self.__name} = {self.__length}, \n водоизмещение = {self.__displacement}, \n скорость в узлах = {self.__max_speed_knots}")

Lincore = ship("Lincore", -250, 53500, 30.8)
Korabl = ship("Pobeda", 10, 120, 20.3)
Korabl_3 = ship("K3", 1000, 20.10, 200.4)
