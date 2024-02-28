class Rabbit:
    def __init__(rabbit,age,weight,color,gender):
        rabbit.age = 0
        rabbit.set_age(age)
        rabbit.weight = 0
        rabbit.set_weight(weight)
        rabbit.color = color
        rabbit.gender = gender

    def set_age(rabbit,age):
        if age<0 :
            print("Ошибка")
        else: 
            rabbit.age = age

    def get_age(rabbit):
        return rabbit.age
    
    def set_weight(rabbit,weight):
        if weight<0 :
            print("Ошибка")
        else: 
            rabbit.weight = weight

    def get_weight(rabbit):
        return rabbit.weight

    def set_color(rabbit,color):
        rabbit.color = color

    def get_color(rabbit):
        return rabbit.color
    
    def set_gender(rabbit,gender):
        rabbit.gender = gender

    def get_gender(rabbit):
        return rabbit.gender
    
    def print_rabb(rabbit):
        print("Возраст кролика", rabbit.get_age(), "вес равен", rabbit.get_weight(), "килограммам, имеет", rabbit.get_color(),"окрас и", rabbit.get_gender(), "пол", "\n------------------------------")