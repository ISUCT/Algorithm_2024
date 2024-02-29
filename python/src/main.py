import sample

if __name__ == "__main__":
    print("lab 5 python")
    sobachka = sample.Dog(age=12, name="Zhychka", gender="male")

    print(f"The dog's name is {sobachka.name}")
    print(f"The dog {sobachka.name} is {sobachka.age} years old")
    print(f"{sobachka.name} is a {sobachka.gender}")
    
