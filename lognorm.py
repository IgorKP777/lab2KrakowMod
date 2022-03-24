import math
import random
import statistics as stat
from matplotlib import pyplot as plt
from prettytable import PrettyTable as pt
import numpy as np


def ln():
    mo = 5
    diss = 1
    n = 1000
    beta = math.sqrt(math.log(1 + (diss / mo ** 2)))
    alfa = math.log(mo) - ((beta ** 2) / 2)
    lt = []
    for i in range(n):
        z = 0
        for y in range(12):
            z += random.uniform(0, 1)
        z -= 6
        y = alfa + beta * z
        x = math.exp(y)
        lt.append(x)
    mean = stat.mean(lt)
    variance = stat.variance(lt)
    standard_deviation = math.sqrt(variance)
    table_result = pt()
    table_result.title = 'Лог-нормальный закон'
    table_result.field_names = ['Параметры оценки', 'Результат']
    table_result.add_row(['alfa', round(alfa, 3)])
    table_result.add_row(['beta', round(beta, 3)])
    table_result.add_row(['Оценка математического ожидания', round(mean, 3)])
    table_result.add_row(['Оценка дисперсии', round(variance, 3)])
    table_result.add_row(['Оценка среднеквадратического отклонения', round(standard_deviation, 3)])
    sigmaN = (1.96 * standard_deviation) / (math.sqrt(n))
    x1N = mean - sigmaN
    x2N = mean + sigmaN
    table_result.add_row(
        ['Доверительный интервал математического ожидания', '(' + str(round(x1N, 3)) + ', ' + str(round(x2N, 3)) + ')'])
    print(table_result)

    graphN = plt
    min1 = min(lt)
    max1 = max(lt)
    frequency = [round(i, 3) for i in np.arange(min1, max1, (min1 + max1) / 40)]
    graphN.hist(x=lt, bins=frequency, edgecolor='white')
    graphN.title('Лог-нормальный закон')
    graphN.xlabel('')
    graphN.ylabel('Частота')
    graphN.show()
