daily_increase = 0.1
day_num = 1

first_day_result = float(input("Введите пожалуйста результат пробега за первый день: "))
goal = float(input("Введите пожалуйста общий требуемый результат: "))

if first_day_result < goal:
    while first_day_result < goal:
        first_day_result += first_day_result * daily_increase
        day_num += 1
    print(f"Результат в {goal} км будет достигнут на {day_num:d}-й день!")
else:
    print("Результат достигнут!")
