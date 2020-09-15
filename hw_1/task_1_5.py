"""
Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная
сумма пополнения вклада. Необходимо в главной функции реализовать вложенную
функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит
средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
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


def get_deposit_sum(first_deposit, countdown, add_sum):
    def add_deposit(add_sum, proc):
        nonlocal countdown
        count = countdown - 2
        add_depo = add_sum * count + (add_sum * count * proc / countdown)
        return add_depo

    spam = 0
    if first_deposit < small['end_sum']:
        if countdown < 24:
            end_deposit = (first_deposit + (first_deposit * small[countdown]) +
                           add_deposit(add_sum, small[countdown]))
        else:
            spam += first_deposit + (first_deposit * small[countdown])
            end_deposit = (spam + (spam * small[countdown]) +
                           add_deposit(add_sum, small[countdown]))
    elif first_deposit < medium['end_sum']:
        if countdown < 24:
            end_deposit = (first_deposit + (first_deposit * medium[countdown]) +
                           add_deposit(add_sum, medium[countdown]))
        else:
            spam += first_deposit + (first_deposit * medium[countdown])
            end_deposit = (spam + (spam * medium[countdown]) +
                           add_deposit(add_sum, medium[countdown]))
    else:
        if countdown < 24:
            end_deposit = (first_deposit + (first_deposit * high[countdown]) +
                           add_deposit(add_sum, high[countdown]))
        else:
            spam += first_deposit + (first_deposit * high[countdown])
            end_deposit = (spam + (spam * high[countdown]) +
                           add_deposit(add_sum, high[countdown]))
    return end_deposit


print(get_deposit_sum(5000, 24, 100))
print(get_deposit_sum(50000, 12, 1000))
print(get_deposit_sum(500000, 24, 10000))
