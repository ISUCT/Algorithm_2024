from cat import Cat


if __name__ == "__main__":
    print('lab 5(python)')
    cat = Cat(3, "Jack", "black and white")
    cat.set_age(5)
    cat.set_name("Tom")
    cat2 = Cat(5, "Tom", "white")

    print(f"Возраст кота - {cat.get_age()}")
    print(f"Его имя - {cat.get_name()}")
    print(f"Его цвет - {cat.get_color()}")

  
