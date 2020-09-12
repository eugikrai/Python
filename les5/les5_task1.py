directory = "adds/"
text_file = "les5_task1.txt"

print("введите пожалуйста строку.")

task_exec = open(directory + text_file, "w", encoding="utf-8")
while True:
    last_string = input(": ")
    if last_string == "":
        break
    else:
        print(last_string, file=task_exec)

task_exec.close()
