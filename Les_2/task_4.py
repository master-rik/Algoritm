"""
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м
включительно. Вывод выполнить в табличной форме:
по десять пар "код-символ" в каждой строке.
"""
Start = 32
Stop = 128  # +1 для включения в диапазон

for i in range(Start, Stop):
    print(f"{i}- {chr(i)}", end='  ')
    if i % 10 == 1:
        print()
