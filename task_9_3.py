class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        super().__init__(name, surname, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus


first_worker = Position('Bob', 'Dilan', 'driver', 1000, 500)

second_worker = Position('Jaf', 'Miller', 'server', 300,  800)

print(first_worker.get_full_name())
print(first_worker.get_total_income())
print('----------------------------------')
print(second_worker.get_full_name())
print(second_worker.get_total_income())

