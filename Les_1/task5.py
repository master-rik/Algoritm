""" 6. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква."""

n = int(input('Введите порядковый номер буквы в алфавите: '))
n = 96 + n
print('Введенная буква', chr(n))
