from __init__ import Cat

if __name__ == "__main__":
    cat1 = Cat(14, "Siamese", "Alice")
    Cat.print_info_cat(cat1)
    cat2 = Cat(2, "British", "Oleg")
    cat3 = Cat(25, "Street", "Anton")
    Cat.print_info_cat(cat2)
    Cat.print_info_cat(cat3)
