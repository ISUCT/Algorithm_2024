class Comp:
    def __init__(self, value: int, name: str, type: str):
        self.value = value
        self.name = name
        self.type = type

    def set_value(self, value: int):
        if value > 128:
            self.value = value
        else:
            print("Слишком маленький объём жёсткого диска")
    def set_name(self, name: str):
        self.name = name
    def set_type(self, type: str):
        self.type = type
    def get_value(self):
        return self.value
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type