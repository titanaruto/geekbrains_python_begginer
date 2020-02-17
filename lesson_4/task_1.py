# -*- coding: utf-8 -*-
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys


def get_salary(hours, rate, prize):
    return (int(hours) * float(rate)) + float(prize)


try:
    file_name, hours_param, rate_param, price_param = sys.argv
    price = get_salary(hours_param, rate_param, price_param)
except Exception as e:
    print(e)
else:
    print(price)
