a = int(input("Введите пожалуйста положительное число: "))

if a < 0:
    a = int(input("Введите пожалуйста положительное число! "))

b = int(str(a) + str(a))
c = int(str(a) + str(b))

d = a + b + c

print(f'{a} + {b} + {c} = {d}')
