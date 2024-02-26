class Fox:
    def __init__(self, name, age, color):
        self._name = name
        self._age = self.set_age(age)
        self._color = color
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_color(self):
        return self._color
    def set_color(self, color: str):
            self._color = color
    def set_age(self, age):
        if age>=0 and age<33:
            self._age = age
        else: 
            raise Exception("foxes don't live so long")
    def new_fox(self):
        print("Name:",self._name, 
              "Age:",self._age, 
              "Color:",self._color)
        if self._name == "Foxy":
            print("""
⣿⣿⣿⣿⣿⡟⣦⣌⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿
⣿⣿⣿⣿⣿⡇⣿⣿⣿⣦⠈⠻⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⢟⣩⣶⣶⡏⠀⣿
⣿⣿⣿⣿⣿⣇⢻⣿⢹⣿⠇⢀⣿⡿⢿⠿⠮⠯⢾⣿⣿⡿⢡⣿⡿⣽⢿⡇⠀⣿
⣿⣿⣿⣿⣿⣿⣌⠛⠛⣫⠜⠋⠁⢠⠁⠀⠀⠀⠀⠀⠛⣷⡈⢿⡿⣃⡾⠁⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣾⠓⠚⠉⠓⡆⠦⠤⠖⣤⡀⠀⠀⢹⣿⣧⣉⣉⣠⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠇⣶⣶⣮⣂⢑⣬⣮⣔⢄⠀⠀⠀⠀⢿⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣥⣭⣿⣼⣿⣿⡙⣇⣂⣀⣀⣀⡈⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠉⠙⠻⢿⣛⠿⡻⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣇⣸⠉⢠⢐⡄⠀⠀⠀⠀⠈⣿⠁⠈⣣⠀⠀⠀⠺⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣿⣭⣵⢤⢤⣤⡤⣤⣶⣾⣿⣤⠴⠃⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢸⡀⣀⣀⣠⣴⣾⣶⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⣿⣿⢟⡟⠁⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠣⣹⣻⣟⠿⠕⠁⢀⣠⣾⡟⠛⠋⠉⡟⠁⠀⠀⠙⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣠⣶⢻⣷⣀⣠⣤⣖⣿⢏⡾⠀⠀⠀⠘⣇⣀⣤⣶⠟⠛⢻⣿⣿⣿
⣿⣿⣿⣿⡿⠉⢸⣯⡴⠻⣋⣛⣛⣻⡏⠃⠀⠀⠀⠸⣿⣿⡟⠁⡠⠂⠁⠀⠉⠻
                  """)