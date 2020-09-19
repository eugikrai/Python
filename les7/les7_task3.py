class MyCell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return MyCell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return MyCell(int(self.quantity - other.quantity))
        else:
            return "Операция вычитания невозможна"

    def __mul__(self, other):
        return MyCell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return MyCell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f"{'*' * cells_in_row} \n"
        row += f"{'*' * (self.quantity % cells_in_row)}"
        return row


cell1 = MyCell(5)
cell2 = MyCell(2)

print(f"Клетка 1: {cell1}")
print(f"Сумма клеток 1 и 2: {cell1 + cell2}")
print(f"Упорядоченная клетка 1 (5):\n{cell1.make_order(5)}")
print(f"Упорядоченная клетка 1 (10):\n{cell1.make_order(10)}")
print(f"Деление клетки 1 на клетку 2: {cell1 / cell2}")
print(f"Разность клетки 2 и 1: {cell2 - cell1}")