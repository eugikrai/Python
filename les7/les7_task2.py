from abc import abstractmethod


class Wear:
    rate = [[6.5, 0.3], [2, 0.3]]

    def __init__(self, title, metric, rate_type):
        self.title = title
        self.size = metric
        self.rate_formula = [self.rate[rate_type][0], self.rate[rate_type][1]]

    @abstractmethod
    def get_cloth_square(self):
        pass


class Clothes(Wear):
    def __init__(self, width, height, rate_type):
        super().__init__(width, height, rate_type)

    @property
    def get_cloth_square(self):
        return self.size / self.rate_formula[0] + self.rate_formula[1]

    def __add__(self, other):
        return self.get_cloth_square + other.get_cloth_square


coat = Clothes("пальто", 4, 0)
suit = Clothes("костюм", 10, 1)

print(f"Всего расход ткани на {coat.title}: {coat.get_cloth_square:.4f}")
print(f"Всего расход ткани на {suit.title}: {suit.get_cloth_square:.4f}")

print(f"Общий расчет расхода ткани: {(coat + suit):.4f}")
