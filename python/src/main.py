# type: ignore
import lab


def summ(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print("Hello world")
    print(summ(3, 4))
    lab = lab.Dog("Bob", 19, 26)
    lab.newDog()
