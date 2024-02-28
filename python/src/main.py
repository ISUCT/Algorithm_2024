from __init__ import Rabbit

if __name__ == '__main__':
    rabb1 = Rabbit(5, 1.5, "Чёрный", "муж")
    rabb2 = Rabbit(7, 2.0, "Белый", "жен")
    Rabbit.print_rabb(rabb1)
    Rabbit.print_rabb(rabb2)