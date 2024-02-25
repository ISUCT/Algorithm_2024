from __init__ import Dog

def main():
    # Создание объекта класса Dog
    my_dog = Dog("Будди", "Золотистый ретривер",   5)

    # Изменение возраста собаки
    my_dog.set_age(10)

    # Вывод обновленного описания собаки
    print(my_dog.describe())

if __name__ == "__main__":
    main()
