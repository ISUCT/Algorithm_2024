import sample

if __name__ == "__main__":
    Cat1 = sample.Cat("Мурка", 10, "девочка")
    Cat1.PrintAllProperty()
    print("---")
    Cat1.setAge(-5)
    Cat1.getAge()
    Cat1.PrintAllProperty()