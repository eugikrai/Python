seasons = ['зима', 'весна', 'лето', 'осень']

calendar = {1: ["январь", seasons[0]], 2: ["февраль", seasons[0]], 3: ["март", seasons[1]], 4: ["апрель", seasons[1]],
            5: ["май", seasons[1]], 6: ["июнь", seasons[2]], 7: ["июль", seasons[2]], 8: ["август", seasons[2]],
            9: ["сентябрь", seasons[3]], 10: ["октябрь", seasons[3]], 11: ["ноябрь", seasons[3]],
            12: ["декабрь", seasons[0]]}
while True:
    mon = int(input("номер месяца (от 1 до 12): "))
    if mon < 1 or mon > 12:
        print("номер месяца (от 1 до 12!")
    else:
        break

print(f"{calendar[mon][0]}, {calendar[mon][1]}")
