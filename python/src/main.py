import lab


def summ(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print("Hello world")
    print(summ(3, 4))
    try:
        my_dog = lab.new_dog(3, 20, "овчарка")
        print("Age:", my_dog.get_age())
        print("Weight:", my_dog.get_ves())
        print("Breed:", my_dog.get_poroda())
    except ValueError as e:
        print("Error:", e)
