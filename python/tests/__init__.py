def print_employee():
    name = input("Введите ваше ФИО")
    data =input("введите число и месц начала работы")
    age = int(input("введите ваш возраст"))
    experience = input("введите стаж работы")
    if age > 18 and age <= 60:
        print(f"работник: {name}, возраст:{age}, стаж;{experience}, года, дата начала работы: {data}")
    else:
        print("у работника неверный возраст")
print_employee()