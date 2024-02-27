import catStruct

if __name__ == "__main__":
    # Чалунин Артём 1/279
    # ----------- Лабораторная работа №6 -----------------
    print('Lab number 6')
    cat1 = catStruct.Cat(10, "Male", "Russian", 'Skaya')
    cat1.name = 'lalal'
    cat1.age = 80
    cat2 = catStruct.Cat(5, "Female", "Scottish lop-eared", "Timosha")
    print(cat2.gender)
