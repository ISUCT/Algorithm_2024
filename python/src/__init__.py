class Gun:
    def __init__(self, name: str, caliber: float, material: str):
        self.__name = name
        self.__caliber = caliber
        self.__material = material
        self.check_caliber(caliber)

    def check_caliber(self, caliber: float):
        if caliber <= 0:
            print("Некорректный калибр пистолета!")
        else:
            self.__caliber = caliber

    
    def name(self):
        return self.__name

   
    def name(self, n: str):
        self.__name = n

    
    def caliber(self):
        return self.__caliber

   
    def caliber(self, c: float):
        self.check_caliber(c)
        self.__caliber = c

 
    def material(self):
        return self.__material

    @material.setter
    def material(self, m: str):
        self.__material = m

    def vivod(self):
        print(f"Название пистолета - {self.__name}")
        print(f"Калибр пистолета - {self.__caliber}")
        print(f"Материал пистолета - {self.__material}")
