class Computer:
    def __init__(self):
        self.name = ""
        self.hard_drive_capacity_gb = 0

    def set_hard_drive_capacity(self, capacity_gb):
        self.hard_drive_capacity_gb = capacity_gb

    def get_hard_drive_capacity(self):
        return self.hard_drive_capacity_gb