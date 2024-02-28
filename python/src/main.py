# type: ignore
import cat

if __name__ == "__main__":
    cat1 = cat.Cat(6, "Tiger", "Siamese")
    cat2 = cat.Cat(9, "No name", "unknown")

    cat1.age = 3

    cat2.name = "Marshal"
    cat1.name = "Luna"

    print("Cat's age is {0}".format(cat1.age))
    print("Its name is {0}".format(cat1.name))
    cat1.petTheCat()

    print("Another cat's age is {0}".format(cat2.age))
    print("Its breed is {0}".format(cat2.breed))
    cat2.petTheCat()
