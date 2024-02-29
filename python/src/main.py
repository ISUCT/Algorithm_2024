#def summ(a: int, b: int) -> int:
#    return a + b


#if __name__ == "__main__":
#    print("Hello world")
#    print(summ(3, 4))

from phonenumber.phone import Phone

def main():
    phone1 = Phone("Iphone", "Black", 9834765873)
    print("Brand:", phone1.get_brand())
    print("Color:", phone1.get_color())
    print("Number", phone1.get_number(), "\n")

    phone2 = Phone("OnePlus", "Gold", 2873469126)
    print("Brand:", phone2.get_brand())
    print("Color:", phone2.get_color())
    print("Number", phone2.get_number(), "\n")

    phone3 = Phone("POCO", "Blue", 1265872364)
    print("Brand:", phone3.get_brand())
    print("Color:", phone3.get_color())
    print("Number", phone3.get_number(), "\n")

if __name__ == "__main__":
    main()
