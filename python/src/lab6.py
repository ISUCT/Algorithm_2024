class Phone:
    def __init__(self, number: int, provider: str, country: str):
        self.number = number
        self.provider = provider
        self.country = country

    def set_number(self, number: int):
        if len(str(number)) == 11:
            self.number = number
        else:
            print("Невозможно установить данный номер, так как его длина не равна 11")
    def set_provider(self, provider: str):
        self.provider = provider
    def set_country(self, country: str):
        self.country = country
    def get_number(self):
        return self.number
    def get_provider(self):
        return self.provider
    def get_country(self):
        return self.country
