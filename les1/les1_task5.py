earn = float(input("Введите пожалуйста общую сумму выручки компании: "))
cost = float(input("Введите пожалуйста общую сумму издержек компании: "))

profit = earn - cost
if profit > 0:
    print(f"Ваша прибыль: {profit:.1f} и рентабельность компании:{profit/earn:.1%}")
    worker = int(input("Введите пожалуйста число ваших сотрудников: "))
    profit_per_worker = profit / worker
    print(f"Прибыль фирмы в расчете на одного сотрудника составила: {profit_per_worker:.1f}")
elif profit < 0:
    print(f"Убыток компании: {profit:.1f}")
