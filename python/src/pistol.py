class Pistol:
    def __init__(self, magazine_capacity: int, model: str, caliber: str):
        if magazine_capacity < 5 or magazine_capacity > 30:
            raise ValueError("Invalid pistol magazine capacity")    
        self.magazine_capacity = magazine_capacity
        self.model = model
        self.caliber = caliber
    
    def set_magazine_capacity(self, magazine_capacity: int):
        if magazine_capacity < 5 or magazine_capacity > 30:
            raise ValueError("Invalid pistol magazine capacity")
        self.magazine_capacity = magazine_capacity
    
    def set_model(self, model: str):
        self.model = model
    
    def set_caliber(self, caliber: str):
        self.caliber = caliber   
    
    def get_magazine_capacity(self) -> int:
        return self.magazine_capacity

    def get_model(self) -> str:
        return self.model

    def get_caliber(self) -> str:
        return self.caliber