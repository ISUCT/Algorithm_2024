import lab
if __name__ == "__main__":
    bludo_1 = lab.Dish(430, 300, "Borsch")
    bludo_1.set_name("Kartoshka")
    bludo_1.set_calorie(200)
    bludo_1.set_price(134)
    bludo_2 = lab.Dish(200, 345, "Olivie")
    bludo_2.set_name("Kraboviy salat")
    bludo_2.set_calorie(320)
    bludo_2.set_price(150)
    bludo_1.print_bludo()
    bludo_2.print_bludo()
    