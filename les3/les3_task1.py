def division(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
        z = 0.0
    return z


x = float(input("Введите числовой аргумент 1: "))
y = float(input("Введите числовой аргумент 2: "))

print("Результат деления: " + str(division(x, y)))
