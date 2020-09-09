from sys import argv


def pay(time, base, bonus):
    return time * base + bonus


try:
    print("Зарплата: {}".format(pay(float(argv[1]), float(argv[2]), float(argv[3]))))
except ValueError:
    print("ДЛя расчета вводить только числа - время в часах, базовая ставка, премия")
