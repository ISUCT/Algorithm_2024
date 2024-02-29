# Kozlov Egor 1/278; Variant 11

class Document:
    def __init__(self, path: str, docType: str, docSize: int):
        if not isinstance(path, str):
            raise TypeError("path must be str")

        if not isinstance(docType, str):
            raise TypeError("docType must be str")

        self.__documentPath = path
        self.__documentType = docType
        self.documentSize = docSize

    @property
    def documentPath(self) -> str:
        return self.__documentPath

    @property
    def documentType(self) -> str:
        return self.__documentType

    @property
    def documentSize(self) -> int:
        return self.__documentSize

    @documentSize.setter
    def documentSize(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("docSize must be int")

        if value < 0:
            raise ValueError(value)

        self.__documentSize = value

    def __str__(self) -> str:
        return f"Document: '{self.documentPath}', '{self.documentType}', {self.documentSize}"


if __name__ == "__main__":
    print("Test 1")
    instance = Document("/media/Files/Script.docx", "docx", 32000)

    print("Test 2")
    try:
        Document(32, "docx", 32000)  # type: ignore
    except Exception as e:
        print("Catched:", e)

    print("Test 3")
    try:
        Document("/media/Files/Script.docx", 128, 32000)  # type: ignore
    except Exception as e:
        print("Catched:", e)

    print("Test 4")
    try:
        Document("/media/Files/Script.docx", "docx", "32000")  # type: ignore
    except Exception as e:
        print("Catched:", e)

    print("Test 5")
    try:
        Document("/media/Files/Script.docx", "docx", -10)
    except Exception as e:
        print("Catched:", e)

    print(str(instance))

    instance.documentSize = 1600

    print(str(instance))

    try:
        instance.documentSize = -18
    except Exception as e:
        print("Catched:", e)

    print(str(instance))
