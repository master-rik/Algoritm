"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random() * 100) - 50)
print(a)

i = 0
index = -1
while i < N:
    if a[i] < 0 and index == -1:
        index = i
    elif a[i] < 0 and not a[i] <= a[index]:
        index = i
    i += 1

print(f"{index + 1} : {a[index]}")
