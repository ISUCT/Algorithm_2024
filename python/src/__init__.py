class Character:
    def __init__(self, name, clas, lvl):
        self.name = name
        self.clas = clas
        if lvl < 0:
            raise 'Начальный уровень не может быть отрицательным'
        else:
            self.lvl = lvl

    def set_name(self, new_name):
        self.name = new_name

    def set_clas(self, new_clas):
        self.clas = new_clas

    def set_lvl(self, new_lvl):
        if new_lvl < 0:
            raise 'Начальный уровень не может быть отрицательным'
        else:
            self.lvl = new_lvl

    def get_name(self):
        return self.name

    def get_clas(self):
        return self.clas

    def get_lvl(self):
        return self.lvl