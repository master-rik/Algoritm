"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
"""

import hashlib


def substrings(n):
    if len(n) == 0 or len(n) == 1:
        return len(n)
    res = set()
    count = 1
    while count < len(n):
        for i in range(len(n)):
            res.add(hashlib.sha1(n[i:i + count].encode('utf-8')).hexdigest())
        count += 1
    return len(res)


user_enters = input("Ваша строка: ")
print(f"Получилось подстрок: {substrings(user_enters)}")
