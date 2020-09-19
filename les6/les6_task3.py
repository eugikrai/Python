class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name.capitalize() + ' ' + self.surname.capitalize()

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('eugen', 'railean', 'developer', 245687, 45686)

print('Name:', a.get_full_name())
print('Position:', a.position)
print('Income: ', a.get_total_income())
