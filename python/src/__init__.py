class Country:
    def __init__(self, name: str, population: int, area: int):
        self.__name = name
        self.__population = population
        self.__area = area
        self.check_population(population)
        self.check_area(area)

    def check_population(self, population: int):
        if population < 0:
            print(f"Вы указали неверное значение населения страны!")
        else:
            self.__population = population

    def check_area(self, area: int):
        if area < 0:
            print(f"Вы указали неверное значение площади страны!")
        else:
            self.__area = area

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n: str):
        self.__name = n

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, a: int):
        self.check_population(a)
        self.__population = a

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, b: int):
        self.check_area(b)
        self.__area = b

    def output(self):
        print(f"Название страны - {self.__name}")
        print(f"Население страны - {self.__population} чел.")
        print(f"Площадь страны - {self.__area} км²")

