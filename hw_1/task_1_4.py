"""
Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть
представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения
процентной ставки для каждого срока. В функции необходимо проверять
принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной
процентной ставке. Функция возвращает сумму вклада на конец срока.
"""

small = {
    'begin_sum': 1000,
    'end_sum': 10000,
    6: 0.05 / 2,
    12: 0.06,
    24: 0.05
}
medium = {
    'begin_sum': 10000,
    'end_sum': 100000,
    6: 0.06 / 2,
    12: 0.07,
    24: 0.065
}
high = {
    'begin_sum': 100000,
    'end_sum': 1000000,
    6: 0.07 / 2,
    12: 0.08,
    24: 0.075
}


def get_deposit_sum(first_deposit, countdown):
    spam = 0
    if first_deposit < small['end_sum']:
        if countdown < 24:
            end_deposit = first_deposit + (first_deposit * small[countdown])
        else:
            spam += first_deposit + (first_deposit * small[countdown])
            end_deposit = spam + (spam * small[countdown])
    elif first_deposit < medium['end_sum']:
        if countdown < 24:
            end_deposit = first_deposit + (first_deposit * medium[countdown])
        else:
            spam += first_deposit + (first_deposit * medium[countdown])
            end_deposit = spam + (spam * medium[countdown])
    else:
        if countdown < 24:
            end_deposit = first_deposit + (first_deposit * high[countdown])
        else:
            spam += first_deposit + (first_deposit * high[countdown])
            end_deposit = spam + (spam * high[countdown])
    return end_deposit


print(get_deposit_sum(5000, 24))
print(get_deposit_sum(50000, 12))
print(get_deposit_sum(500000, 24))
