import lab_struct

if __name__=="__main__":
    print("Коротков Михаил Александрович 1/278")
    print("Рабочий 1")
    work1=lab_struct.Worker("Влад", "Хирург", 40000)
    work1.come()
    print(work1.salary)
    work1.salary=30000
    print(work1.salary)
    del work1


    print("Рабочий 2")
    work2=lab_struct.Worker("Леонардо", "Уборщик", 13000)
    print(work2)