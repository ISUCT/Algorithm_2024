from structure import klass

if __name__ == "__main__":
    print(f"{klass.Lincore.length}")
    print(f"{klass.Lincore.name}")

    Korabl_2 = klass.ship("K2", -130.4, 40.8, 100)
    klass.ship.output(Korabl_2)
    print(f"{Korabl_2.name}")
    klass.ship.output(klass.Korabl_3)

    klass.ship.Sail(klass.Lincore)

    klass.ship.output(Korabl_2)

    klass.ship.output(klass.Lincore)

    klass.Lincore.length = -100
    print(klass.Lincore.name)

    print(f"{klass.Lincore.name}")
    print(f"{klass.Lincore.length}")