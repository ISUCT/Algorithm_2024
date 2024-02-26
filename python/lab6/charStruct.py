class Char():
    __power = 0
    __mana = 0
    __name = ''

@property
def power(self) -> int:
    return self.__power

@power.setter
def power(self, power):
    assert (power >= 0 and power <= 100), "invalid Power"
    self.__power = power

@property
def mana(self) -> int:
    return self.__mana

@mana.setter
def mana(self, mana):
    assert (mana >= 0 and mana <= 100), "invalid Mana"
    self.__mana = mana

@property
def name(self) -> str:
    return self.__name

@name.setter
def name(self, name):
    self.__name = name

def helloWorld(self):
    print("Character {0} says HELLO WORLD!\n".format(self.__name))