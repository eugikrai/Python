directory = "adds/"
text_file = "les5_task1.txt"

a = 0
words = []
with open(directory + text_file, "r", encoding="utf-8") as task_exec:
    r_str = task_exec.readlines()

print(f"всего строк: {len(r_str)}")
for a in r_str:
    words.append(len(a.split(" ")))

print(f'всего слов: {words}')
