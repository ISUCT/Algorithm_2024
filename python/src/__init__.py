class Document:
    def __init__(self, document_type, size, year_of_creation):
        self.document_type = document_type
        self.size = 0
        self.set_size(size)
        self.year_of_creation = year_of_creation

    def set_size(self, size):
        if size <= 0:
            raise "Размер не может быть 0 или меньше"
        else:
            self.size = size

    def set_document_type(self, document_type):
        self.document_type = document_type

    def set_year_of_creation(self, year_of_creation):
        self.year_of_creation = year_of_creation

    def get_document_type(self):
        return self.document_type

    def get_size(self):
        return self.size

    def get_year_of_creation(self):
        return self.year_of_creation

    def delete_document(self):
        print(f"Документ {self.document_type} отправлен в корзину")
