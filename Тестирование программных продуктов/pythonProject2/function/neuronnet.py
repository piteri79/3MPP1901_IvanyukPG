# coding: utf-8
## Полносвязная нейронная сеть

# подключение библиотек
import math
from random import random


# Класс нейрон
class neuron:
    def __init__(self, x):
        self.__x = x
        self.__net = 0.0
        self.__y = 0.0

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def calc(self):
        if type(self.__x) == list:
            # Цикл суммирования
            for i in self.__x:
                self.__net += i[0].get_y() * i[1]
            # Цикл активации
            if self.__net >= 0.5:
                self.__y = 1
            else:
                self.__y = 0
            self.__net = 0.0
        else:
            self.__y = self.__x


# Построение нейронной сети
class net:
    def __init__(self, *args):
        self.__wcount = args  # Список переданных аргументов
        self.__NN = []  # Список всей сети
        for i in self.__wcount:
            self.__NN.append([neuron([]) for n in range(i)])
        for i in range(len(self.__NN)):
            for n in self.__NN[i]:
                n.set_x(0.0) if i == 0 else n.set_x([[x, random()] for x in self.__NN[i - 1]])

    def summary(self):
        iii = []
        for i in range(len(self.__NN)):
            print('\n============ Слой нейронной сети:', i + 1, '=================')
            if i > 0:
                print('Нейронов=', len(self.__NN[i]))
                ii = len(self.__NN[i]) * len(self.__NN[i - 1])
                iii.append(ii)
                print('Вычисляемых параметров=', ii)
        print('==================================================')
        print('Всего вычисляемых параметров=', sum(iii))

    def weights(self, a, b, c, d):
        q = self.__NN[a][b].get_x()
        q[c][1] = d
        self.__NN[a][b].set_x(q)

    def predict(self, a):
        for i, j in zip(self.__NN[0], a): i.set_x(float(j))
        for i in range(len(self.__NN)):
            for j in self.__NN[i]: j.calc()
        n = [n.get_y() for n in self.__NN[-1]]
        return n
