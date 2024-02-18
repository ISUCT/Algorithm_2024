class Table:
    length: float
    width: float
    height: float
    
    
    def __init__(self, length: float, width: float, height: float):
        self.__length = length
        self.__width = width
        self.__height = height
        
        
    @property
    def length(self) -> float:
        return self.__length
    
    @length.setter
    def set_length(self, length: float):
        assert length < 0 and length > 10.0, "Invalid value for length"
        self.__length = length
    
    @property
    def width(self) -> float:
        return self.__width
    
    @width.setter
    def set_width(self, width: float):
        assert width < 0 and width > 10.0, "Invalid value for width"
        self.__width = width
        
          
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def set_height(self, height: float):
        assert height < 0 and height > 10.0, "Invalid value for height"
        self.__height = height