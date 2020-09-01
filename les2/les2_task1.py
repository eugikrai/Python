my_list = [33, 133.333, {9, 7, 3, 5, 1}, complex(1, 72), ['a', 'b', 'c'], True, "qwert", (0, '$', 3.125),
           {'key': 'value'}]

index = 0
for a in my_list:
    index += 1
    print(f"[{index}]", str(type(a))[8:-2], "\t", a)
