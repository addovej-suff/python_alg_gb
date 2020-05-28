# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict


company_count = int(input('Введите количество предприятий: '))

companies = defaultdict(float)
for _ in range(company_count):
    name = input('Название: ')
    for q in range(4):
        profit = float(input(f'Квартал {q + 1}: '))
        companies[name] += profit

# Round to decimal
avg = round(sum(companies.values()) / len(companies), 2)

above_avg = [key for key, val in companies.items() if val > avg]
below_avg = [key for key, val in companies.items() if val < avg]

# If profits of all companies will equals then their profits will be equal average profit
eq_avg = [key for key, val in companies.items() if val == avg]


above_avg_msg = f'Компании с прибылью выше среднего: {", ".join(above_avg)}' \
    if above_avg else 'Нет компаний с прибылью выше среднего'

below_avg_msg = f'Компании с прибылью ниже среднего: {", ".join(below_avg)}' \
    if above_avg else 'Нет компаний с прибылью ниже среднего'


print(f'Средняя прибыль за год по всем предприятиям: {avg}')
print(above_avg_msg, below_avg_msg, sep='\n')
if eq_avg:
    print(f'Компании с прибылью равной средней: {", ".join(eq_avg)}')
