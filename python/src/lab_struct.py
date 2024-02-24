class Worker:
    def __init__(self, name, status: str, salary_worker: int):
        self.__name: str = name
        self.__status: str = status
        try:
            self.__salary: int = checkSalary(salary_worker)
        except ValueError as error:
            print(str(error))
    
    def __del__(self):
        print(f"{self.__name} был удалён")

    def __str__(self) -> str:
        return (f'Имя: {self.__name} Ранг: {self.__status} Зп {self.__salary}')

    def come(self):
        print(f"{self.__name} пришёл на работу.")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def status(self) -> str:
        return self.__status

    @property
    def salary(self) -> int:
        return self.__salary

    @name.setter
    def name(self, name: str):
        self.__name: str = name

    @status.setter
    def status(self, status: str):
        self.__status: str = status

    @salary.setter
    def salary(self, salary: int):
        self.__salary: int = checkSalary(salary)


def checkSalary(salary: int) -> int:
    if (salary >= 15000):
        return salary
    raise ValueError("Ошибка: Минимальная зарплата 15000")