class ClassEx(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
print("'stop' to terminate")

while True:
    x = input("enter the number: ")

    try:
        if x == 'stop':
            break
        my_list.append(float(x))

    except Exception as err:
        print(ClassEx(err))
    finally:
        pass

print(my_list)
