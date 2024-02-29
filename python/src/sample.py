class Document:
    type_of_document: str
    size_of_document: int
    title_of_document: str
    
    
    def __init__(self, type_of_document: str, size_of_document: int, title_of_document: str, types: list):
        self.__type_of_document = type_of_document
        self.__size_of_document = size_of_document
        self.__title_of_document = title_of_document
        
        
    @property
    def type_of_document(self) -> str:
        return self.__type_of_document
    
    @type_of_document.setter
    def set_type_of_document(self, type_of_document: str, types: list):
        assert type_of_document.upper in types, "Invalid type of document"
        self.__type_of_document = type_of_document
    
    @property
    def size_of_document(self) -> int:
        return self.__size_of_document
    
    @size_of_document.setter
    def set_size_of_document(self, size_of_document: int):
        assert size_of_document <= 0, "Invalid size of document"
        self.__size_of_document = size_of_document
        
          
    @property
    def title_of_document(self) -> str:
        return self.__title_of_document

    @title_of_document.setter
    def set_title_of_document(self, title_of_document: str):
        assert len(title_of_document) < 0 or len(title_of_document) > 50, "Invalid title of document"
        self.__title_of_document = title_of_document