from functools import reduce


def new_func(x, y,):
    return x * y


new_list = [x for x in range(100, 1001) if x % 2 == 0]

print(reduce(new_func, new_list))
