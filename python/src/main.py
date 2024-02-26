import lab5

ap1 = lab5.Airplane("Russian airplane", 3, "Russia")
ap2 = lab5.Airplane("Some Airbus", 853, "France")

try:
    ap1.set_speed(11111)
except Exception as error:
    print("Error occured:", error)

ap1.print_airplane()