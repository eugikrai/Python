class ClassEx(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    x = float(input("Please enter a number: "))
    z = float(input("Please enter a divisor: "))
    if not z:
        raise ClassEx("Cannot divide by zero, enter another number: ")
except ClassEx as err:
    print(err)
else:
    print(f"{x / z:.4}")
