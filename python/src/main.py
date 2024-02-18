import structure

if __name__ == "__main__":
    tom = structure.Employee("Tom", 45, "01.03.2022")
    michael = structure.Employee("Michael", 20, "14.08.2024")
    print(tom.print_employee())
    print(michael.print_employee())
