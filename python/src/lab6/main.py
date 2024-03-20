import mouse

if __name__ == "__main__":
    m1 = mouse.Mouse(5, "Ъ", 5)
    m2 = mouse.Mouse(3, "Golang", 30)

    print("The name of the first mouse is {0}".format(m1.name))
    print("the age of the first mouse {0}".format(m1.age))

    print("The name of the second mouse is {0}".format(m2.name))
    print("the age of the second mouse {0}".format(m2.age))
    
    m1.mouseSqwueaking()
    m2.mouseSqwueaking()