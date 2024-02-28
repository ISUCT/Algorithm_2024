from pistol import Pistol


if __name__ == "__main__":
    #print("Hello world")
    #print(summ(3, 4))
    
    # Хосровян Александр Арменович 1/279
    print("Lab 1 on python:")
    
    pistol1 = Pistol(9, "Desert Eagler", ".357 Magnum")
    pistol2 = Pistol(15, "...", "...")
    
    pistol2.set_model("Glock")
    pistol1.set_model("Revolver")
    
    pistol1.set_magazine_capacity(6)
    pistol2.set_caliber("9х19 Luger")
    
    print("Pistol 1")
    print("Модель пистолета - {}".format(pistol1.get_model()))
    print("Ёмкость магазина - {}".format(pistol1.get_magazine_capacity()))
    print("Калибр - {}".format(pistol1.get_caliber()))
    
    print("Pistol 2")
    print("Модель пистолета - {}".format(pistol2.get_model()))
    print("Ёмкость магазина - {}".format(pistol2.get_magazine_capacity()))
    print("Калибр - {}".format(pistol2.get_caliber()))