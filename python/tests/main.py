import Lab5 as laba

Mouse = input("Введите имя мыша: ")
Age = int(input("Введите возраст мыша: "))
Gender = input("Введите пол мыша: ")
Color = input("Введите цвет мыша: ")

Mysh1 = laba.Mouse(Mouse, Age, Color, Gender)

Mysh1.get()
