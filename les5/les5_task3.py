directory = "adds/"
text_file = "les5_task3.txt"

with open(directory + text_file, "r", encoding="utf-8") as task_exec:
    r_str = task_exec.readlines()

payment = []
average = 0
for a in r_str:
    payment = a.rstrip().split(" ")
    if float(payment[1]) < 20000:
        print(f"{payment[0]} -> {payment[1]}")
    average += float(payment[1])

print(f"средней величины дохода сотрудников : {average / len(r_str)}")