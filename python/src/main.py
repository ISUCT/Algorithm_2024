from __init__ import Document

if __name__ == "__main__":
    document_1 = Document("Договор", 1240, 1980)
    document_1.set_document_type("Согласие")
    document_1.set_year_of_creation(2005)
    print(document_1.get_document_type(), document_1.get_year_of_creation())
    document_2 = Document("Лицензия", 550, 2048)
    print(document_2.get_document_type(), document_2.get_size())
    document_2.delete_document()
