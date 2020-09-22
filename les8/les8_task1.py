from datetime import datetime


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def convert(cls, day_month_year):
        my_date = day_month_year.split("-")
        return int(my_date[0].strip()), int(my_date[1].strip()), int(my_date[2].strip())

    @staticmethod
    def validate(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError as err:
            return f'Error: {err}'
        else:
            return f'Correct date'

    def __str__(self):
        return f'Current date {self.convert(self.day_month_year)}'


today = Date('20 - 9 - 2020')

print(today)
print(Date.validate(1, 1, 2021))
print(today.validate(1, 2, 2022))
print(Date.convert('1 - 1 - 2021'))
print(today.convert('1 - 2 - 2022'))
print(Date.validate(1, 1, 2021))
