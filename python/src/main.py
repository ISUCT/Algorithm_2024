import sample

if __name__ == "__main__":
    print("lab 5")
    
    types = ("DOCX", "DOC", "DOTX", "DOT", "RTF", "TXT", "HTM", "PDF", "DOCM", "DOTM", "XML", "MHT", "DIC", "THMX")
    documentik = sample.Document(type_of_document="docx", size_of_document=300, title_of_document="failik", types=types)
    
    print("The document type is {0}".format(documentik.type_of_document))
    print("The document size is {0} bites".format(documentik.size_of_document))
    print("The document title is {0}".format(documentik.title_of_document))