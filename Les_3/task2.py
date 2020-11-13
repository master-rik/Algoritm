"""
3. В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""

from random import random

N = 10
a = [0] * N
for i in range(N):
    a[i] = int(random() * 1000)
    print(a[i], end=' ')
print()

mn = 0
mx = 0
for i in range(N):
    if a[i] < a[mn]:
        mn = i
    elif a[i] > a[mx]:
        mx = i
print(f'[{mn + 1}]:{a[mn]}, [{mx + 1}]:{a[mx]}')
