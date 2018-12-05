import random


class Dreidel:

    def __init__(self):
        self.__sides = ['Nun', 'Gimmel', 'Hei', 'Shin']
        self.__side_up = 'Gimmel'

    def spin(self):
        #input("Spinning... (press Enter to stop) ")
        letter = random.randint(0, 3)
        self.__side_up = self.__sides[letter]
        return  letter

    def get_side_up(self):
        return self.__side_up
