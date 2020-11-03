""" Написать программу, которая генерирует в указанных пользователем
границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import random

n_random = random()

min_n = int(input())
max_n = int(input())
n = int(n_random * (max_n - min_n + 1)) + min_n
print(n)

min_n = float(input())
max_n = float(input())
n = n_random * (max_n - min_n) + min_n
print(round(n, 2))

min_n = ord(input())
max_n = ord(input())
n = int(n_random * (max_n - min_n + 1)) + min_n
print(chr(n))
