import charStruct

if __name__ == "__main__":
    char1 = charStruct.Char(25, 25, "Goshan")
    char2 = charStruct.Char(70, 85, "Luna")

    char1.mana = -1

    char1.name = "Goshechka"
    char2.name = "Lunarita"

    print("Character name is {0}".format(char1.name))
    print("charscter mana points is {0}".format(char1.mana))
    print("charscter power points is {0}".format(char1.power))
    char1.helloWorld

    print("Character name is {0}".format(char2.name))
    print("charscter mana points is {0}".format(char2.mana))
    print("charscter power points is {0}".format(char2.power))
    char2.helloWorld