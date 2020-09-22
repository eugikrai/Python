
class ClassEx(Exception):
    def __init__(self, txt):
        self.txt = txt


class OutOfStock(ClassEx):
    pass


class LackOff(ClassEx):
    pass


class Stock:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.balance = []

    def receive(self, equipment, quantity):
        if equipment in self.items:
            index = self.items.index(equipment)
            self.balance[index] = self.balance[index] + quantity
        else:
            self.items.append(equipment)
            self.balance.append(quantity)

    def giveaway(self, equipment, quantity):
        try:
            if equipment not in self.items:
                raise OutOfStock(equipment)
            index = self.items.index(equipment)
            if self.balance[index] < quantity:
                raise LackOff(equipment)
            else:
                self.balance[index] -= quantity
        except OutOfStock:
            print(f"Out of {equipment.name}")
        except LackOff:
            print(f"No such quantity of {equipment.name}")

    def transfer(self, equipment, quantity, other_store):
        self.giveaway(equipment, quantity)
        other_store.receive(equipment, quantity)

    def __str__(self):
        store_list = f"Stock {self.name}:\n"
        if self.items:
            for i, item in enumerate(self.items):
                store_list += f"{i+1}: {item}: {self.balance[i]}\n"
        else:
            store_list += "empty"
        return store_list


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, price {self.price}"


class Printer(OfficeEquipment):
    def __init__(self, name, price, color=False):
        super().__init__(name, price)
        self.color = color

    def __repr__(self):
        s = super().__str__()
        return f"{s}, color: {self.color}"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, dpi):
        super().__init__(name, price)
        self.dpi = dpi

    def __repr__(self):
        s = super().__str__()
        return f"{s}, scanner resolution: {self.dpi}"


class Xerox(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def __repr__(self):
        s = super().__str__()
        return f"{s}, copy speed: {self.speed}"


Stock_A = Stock("main")
Stock_B = Stock("other")

printer_a = Printer("Printer", 100, True)
scanner_a = Scanner("Scanner A", 300, 1400)
scanner_b = Scanner("Scanner B", 230, 700)
xerox_a = Xerox("Xerox A", 200, 10)
xerox_b = Xerox("Xerox B", 200, 10)

print(printer_a, scanner_a, scanner_b, xerox_a, xerox_b, " ", sep="\n")

Stock_A.receive(printer_a, 38)
Stock_A.receive(scanner_a, 421)
Stock_B.receive(scanner_b, 78)
Stock_A.receive(xerox_a, 458)
Stock_A.receive(xerox_b, 41)
Stock_A.receive(xerox_b, 789)

print(Stock_A)
print(Stock_B)

Stock_A.giveaway(xerox_b, 25)

Stock_A.transfer(xerox_b, 8, Stock_B)


print(Stock_A)
print(Stock_B)

Stock_A.transfer(xerox_b, 4562, Stock_B)

Stock_A.transfer(scanner_b, 4566, Stock_B)
