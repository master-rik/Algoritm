"""
3. Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


# n = int(input("Введите число: "))

def funk(n):
    if n == 0:
        return " "  # базовый случай

    if n > 0:
        k = 0
        k = n % 10 + k * 10
        return f"{k}{funk(n // 10)}"


print(funk(3486))
