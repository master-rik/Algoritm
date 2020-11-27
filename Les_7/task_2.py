"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


if __name__ == '__main__':
    size = 10
    array = [random.uniform(0, 50) for _ in range(size)]
    random.shuffle(array)
    print(f'Генерированный массив: {array}')
    array = merge_sort(array)
    print(f'Отсортированнный массиив: {array}')
