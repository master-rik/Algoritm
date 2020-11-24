"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
"""

"""
задача. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""



import sys


def show(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t', f'{type(x)=}, {sys.getsizeof(x)=},{x=}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show(key, level + 1)
                result_size += show(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show(item, level + 1)
    return result_size


def var_size(local_var):
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show(local_variables_dict[var])
    print(f'Список всех переменных: {local_variables_dict}')
    return print(f'Общий размер используемых переменных в функции: {size_of_all_variables} байт')


# Функция поиска буквы по номеру из алфавита, представленного строкой
def funk_1(n):
    abc = 'abcdefghijklmnopqqrstuvwxyz'
    local_variables_dict = locals().copy()
    var_size(local_variables_dict)
    if n <= 0 or n > len(abc):
        return 'ошибка'
    else:
        return print("Это буква", abc[n - 1].upper())


# Функция поиска буквы по ее номеру в кодировке
def funk_2(n):
    local_variables_dict = locals().copy()
    var_size(local_variables_dict)
    if (n + 96) < 97 or (n + 96) > 122:
        return 'ошибка'
    else:
        return print("Это буква", chr(n + 96).upper())


# Функция поиска буквы по номеру из алфавита, представленного списком
def funk_3(n):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    local_variables_dict = locals().copy()
    var_size(local_variables_dict)
    return print("Это буква", abc[n - 1].upper())


funk_1(5)
print('-' * 28, "\n")
funk_2(5)
print('-' * 28, "\n")
funk_3(5)

"""
/home/kant/PycharmProjects/Algoritm/venv/bin/python /home/kant/PycharmProjects/Algoritm/Les_6/task_1.py
	 type(x)=<class 'dict'>, sys.getsizeof(x)=232,x={'n': 5, 'abc': 'abcdefghijklmnopqqrstuvwxyz'}
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='n'
	 type(x)=<class 'int'>, sys.getsizeof(x)=28,x=5
	 type(x)=<class 'str'>, sys.getsizeof(x)=52,x='abc'
	 type(x)=<class 'str'>, sys.getsizeof(x)=76,x='abcdefghijklmnopqqrstuvwxyz'
Список всех переменных: {'local_var': {'n': 5, 'abc': 'abcdefghijklmnopqqrstuvwxyz'}}
Общий размер используемых переменных в функции: 438 байт
Это буква E
"""
# ---------------------------------------------------------------------------------
"""
     type(x)=<class 'dict'>, sys.getsizeof(x)=232,x={'n': 5}
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='n'
	 type(x)=<class 'int'>, sys.getsizeof(x)=28,x=5
Список всех переменных: {'local_var': {'n': 5}}
Общий размер используемых переменных в функции: 310 байт
Это буква E
"""
# ---------------------------------------------------------------------------------
"""

	 type(x)=<class 'dict'>, sys.getsizeof(x)=232,x={'n': 5, 'abc': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='n'
	 type(x)=<class 'int'>, sys.getsizeof(x)=28,x=5
	 type(x)=<class 'str'>, sys.getsizeof(x)=52,x='abc'
	 type(x)=<class 'list'>, sys.getsizeof(x)=264,x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='a'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='b'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='c'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='d'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='e'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='f'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='g'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='h'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='i'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='j'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='k'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='l'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='m'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='n'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='o'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='p'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='q'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='r'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='s'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='t'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='u'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='v'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='w'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='x'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='y'
	 type(x)=<class 'str'>, sys.getsizeof(x)=50,x='z'
Список всех переменных: {'local_var': {'n': 5, 'abc': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}}
Общий размер используемых переменных в функции: 1926 байт
Это буква E
"""

"""
Вывод:
1. меньше всего занимает памяти funk_2, 310 байт
2. самая прожорливая функция это  funk_3, 1926 байт
"""