# type: ignore
import rabbitStruct

if __name__ == "__main__":
    rabbit = rabbitStruct.Rabbit("Benjamin", 5, 3)

    try:
        rabbitStruct.Rabbit(55, 5, 3)
    except Exception as e:
        print("error:", e)

    try:
        rabbitStruct.Rabbit("Dima", 10.5, 7)
    except Exception as e:
        print("error:", e)

    try:
        rabbitStruct.Rabbit("Alice", 20, 15)
    except Exception as e:
        print("error:", e)

    print(str(rabbit))
