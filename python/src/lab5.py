class Table: 
    def __init__(self, lenght: int, width: int, type: str): 
        self.lenght = lenght 
        self.width = width 
        self.type = type 
    def set_lenght(self, lenght: int): 
        if lenght > 520: 
            self.lenght = lenght 
        else: 
            print("Стол не помещается в комнату") 
    def set_width(self, width: int): 
        self.width = width 
    def set_type(self, type: str): 
        self.type = type 
    def get_lenght(self): 
        return self.lenght 
    def get_width(self): 
        return self.width 
    def get_type(self): 
        return self.type