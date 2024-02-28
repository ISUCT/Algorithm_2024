# type: ignore
import lab


def summ(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print("Hello world")
    print(summ(3, 4))
    bunny = lab.Bunny("Bunny", 10, 6000)
    bunny.display_info()
