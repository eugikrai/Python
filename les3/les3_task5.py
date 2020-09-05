def my_func(*sum):
    start = 0
    for a in sum:
        if a != 'x':
            try:
                start += float(a)
            except ValueError:
                print("Введите числа или x")
        else:
            break
    return start


print("Введите числа через пробел и Enter для суммирования\nСимвол x завершит операцию")
first = 0

while True:
    add_num = input("Вводите числа: ").split()
    last = my_func(*add_num)

    first += last
    print(f"Последняя сумма {last} (Общая сумма {first}) ")

    if add_num.count('x'):
        break
