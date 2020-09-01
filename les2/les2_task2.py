a = input("Запишите пожалуйста любые значения через запятую: ")
a_list = [b.lstrip() for b in a.split(',')]

print("До обмена местами:", a_list)

final = None
if len(a_list) % 2:
    final = a_list.pop()

q = 0
for b in a_list:
    if (q % 2) == 0:
        a_list.insert(q, a_list.pop(q + 1))
    q += 1

if final:
    a_list.append(final)

print("После обмена местами:", a_list)
