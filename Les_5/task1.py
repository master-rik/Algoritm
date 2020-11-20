"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

n = int(input('Введите количество предприятий: '))
Company = namedtuple('Company', 'name, profit')
result = []
total = 0

if n != 0:
    for comp in range(n):
        name = input(f'Введите название {comp + 1} предприятия :')
        profit = 0
        for i in range(4):
            profit += float(input(f'Введите прибыль предприятия за {i + 1} квартал: '))
        result.append(Company(name, profit))
        total += profit

    middle_profit = total / n
    print(f'Средняя прибыль = {middle_profit}')

    for company in result:
        if company[1] > middle_profit:
            print(f'предприятие {company[0]} имеет прибыль выше среднего, которая равна {company[1]}')

    for company in result:
        if company[1] < middle_profit:
            print(f'предприятие {company[0]} имеет прибыль ниже среднего, которая равна {company[1]}')
else:
    print("The end!")