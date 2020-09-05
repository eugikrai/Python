def func(a, b, c):
    my_list = [float(a), float(b), float(c)]
    my_list.remove(min(my_list))
    return sum(my_list)


my_num = input("Введите три числа через пробел: ")
my_num_split = my_num.split()

try:
    for x in my_num_split:
        float(x)
    print(func(my_num_split[0], my_num_split[1], my_num_split[2]))
except ValueError:
    print("Либо введено не число, либо не через пробел")
except IndexError:
    print("Вы не ввели три числа")
