from random import randint

class Character:
    def __init__(self, name, intellect, psyche, physique, motorics):
        self.__name = name 
        self.__intellect = intellect 
        self.__psyche = psyche
        self.__physique = physique 
        self.__motorics = motorics   
    
    @property
    def name(self):
        return self.__name

    
    @property
    def intellect(self):
        return self.__intellect
    
    @intellect.setter
    def intellect(self, intellect):
        if 0 < intellect < 11:
            self.__intellect = intellect
        else:
            print("Количество очков интеллекта может быть только от 1 до 10.")

    
    @property
    def psyche(self):
        return self.psyche
    
    @psyche.setter
    def psyche(self, psyche):
        if 0 < psyche < 11:
            self.__psyche = psyche
        else:
            print("Количество очков психики может быть только от 1 до 10.")    

    
    @property
    def physique(self):
        return self.physique
    
    @physique.setter
    def physique(self, physique):
        if 0 < physique < 11:
            self.__physique = physique
        else:
            print("Количество очков физиологии может быть только от 1 до 10.") 
    

    @property
    def motorics(self):
        return self.motorics
    
    @motorics.setter
    def motorics(self, motorics):
        if 0 < motorics < 11:
            self.__motorics = motorics
        else:
            print("Количество очков моторики может быть только от 1 до 10.") 


    def print_overall_info(self):
        if 0 < self.__intellect < 11 and 0 < self.__psyche < 11 and 0 < self.__physique < 11 and 0 < self.__motorics < 11:
            print(f"Имя: {self.__name}\nИнтеллект: {self.__intellect}\nПсихика: {self.__psyche}\nФизиология: {self.__physique}\nМоторика: {self.__motorics}\n")
        else:
            print("Параметры персонажа были заданы неверно: характеристики могут принимать значения только от 1 до 10.")
    
    def event(self):
        if 0 < self.__intellect < 11 and 0 < self.__psyche < 11 and 0 < self.__physique < 11 and 0 < self.__motorics < 11:   
            a = randint(4, 53)
            b = randint(2, 13)
            all = self.__intellect + self.__psyche + self.__physique + self.__motorics
            if (all + b)>= a:
                print(f"Событие пройдено успешно.\nБыло необходимо очков:{a}\nСумма характеристик составила:{all}\nКубики выбросили число:{b}\nСумма ваших очков:{all + b}") 
            else:
                print(f"Событие провалено.\nБыло необходимо очков:{a}\nСумма характеристик составила:{all}\nКубики выбросили число:{b}")
        else:
            print("Параметры персонажа были заданы неверно: характеристики могут принимать значения только от 1 до 10.")



