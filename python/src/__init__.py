class boat():
    name : str = ""
    lifting_Capacity : int = 0
    max_speed_knots : float = 0.0

    def flooding(self,cargo_Weight):
        if cargo_Weight > self.lifting_Capacity:
            print(f"The {self.name} sank due to too heavy cargo")
    def move(self):
        print(f"The {self.name} is moving at a speed of {self.max_speed_knots} Knots per hour")
    def __init__(self, name, lift, speed) -> None:
        self.name = name
        self.lifting_Capacity = lift
        self.max_speed_knots = speed