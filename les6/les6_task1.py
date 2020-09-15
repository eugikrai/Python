from time import sleep


class TrafficLight:
    __color = ['', 'красный ', 'желтый ', 'зеленый ']
    __ansi = ['\033[0m', '\033[31m', '\033[33m', '\033[32m']
    __length = [1, 1, 1, 1]

    def __init__(self, l1=7, l2=7, l3=2):
        self.__length[1] = l1
        self.__length[2] = l2
        self.__length[2] = l3

    def running(self):
        i = 1
        while i <= 3:
            print(f'{self.__ansi[i]}{self.__color[i]}{self.__ansi[0]}')
            sleep(self.__length[i])
            i += 1


TrafficLight = TrafficLight(7, 7, 2)
TrafficLight.running()
