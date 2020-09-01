my_list = [7, 5, 3, 3, 2]

while True:
    my_str = input("Введите число: ")
    if my_str.isdecimal():
        number = int(my_str)
        if len(my_list) != 0:
            if number > my_list[0]:
                my_list.insert(0, number)
            elif number <= my_list[-1]:
                my_list.append(number)
            else:
                for i, el in enumerate(my_list[:-1]):
                    if my_list[i] >= number > my_list[i + 1]:
                        my_list.insert(i + 1, number)
                        break
        else:
            my_list.append(number)
    else:
        break
    print(my_list)
