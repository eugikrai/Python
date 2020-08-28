num = int(input("Введите целое положительное число: "))
if num < 0:
    num = int(input("Введите пожалуйста положительное число! "))
max_num = num % 10

while (num % 10) > 0:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10

print(f"В вашем числе самая большая цифра {max_num}")
