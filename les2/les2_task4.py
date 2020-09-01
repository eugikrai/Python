a = input("Введите несколько слов через пробел: ")
my_list = a.split()

for i, el in enumerate(my_list):
    print(i, el[:10] if (len(el) >= 10) else el)