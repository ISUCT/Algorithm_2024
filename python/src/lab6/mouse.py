class Mouse():
    __age = 0
    __name = ""
    __size = 0
    
    def __init__(self, age, name, size):
        self.age = age
        self.__size = size
        self.__name = name
        
    def mouseSqwueaking(self):
        print("mouse {0} beeping\n".format(self.__name))
    
    def age(self) -> int:
        return self.__age
    
    def age(self, age):
        assert(age >= 0 and age <= 10), "invalid age"
        self.__age = age
        
    def size(self) -> int:
        return self.__size
        
    def size(self, size):
        assert(size >= 6 and size <= 80), "invalid size"
        self.__size = size
        
    def name(self) -> str:
        return self.__name
    
    def name(self, name):
        self.__name = name