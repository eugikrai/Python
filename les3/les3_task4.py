def my_func(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    z = my_func(x, y // 2)
    z *= z
    if y % 2:
        z *= x
    return z


x = float(input("Введите положительное число: "))
y = float(input("Введите целое отрицительное число: "))

print(my_func(x, y))