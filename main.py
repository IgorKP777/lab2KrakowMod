import random as r
import math as m
import numpy as np
import statistics as stat
from matplotlib import pyplot as plt
from prettytable import PrettyTable as pt


if __name__ == '__main__':

    n = 10000
    mo = 10000
    kv = 0.1

    # нормальное распределение
    selectionNormalDistribution = list(np.random.normal(loc=mo, scale=1000, size=n))
    averageN = stat.mean(selectionNormalDistribution)
    varianceN = stat.variance(selectionNormalDistribution)

    standardDeviationN = m.sqrt(varianceN)

    sigmaN = (1.96 * standardDeviationN) / (m.sqrt(n))
    x1N = averageN - sigmaN
    x2N = averageN + sigmaN
    table_result = pt()
    table_result.title = 'Нормальный закон'
    table_result.field_names = ['Параметры оценки', 'Результат']
    table_result.add_row(['m', mo])
    table_result.add_row(['kv', kv])
    table_result.add_row(['n', n])
    table_result.add_row(['Оценка мат ожидания', round(averageN, 3)])
    table_result.add_row(['Оценка дисперсии', round(varianceN, 3)])
    table_result.add_row(['Оценка среднеквадратического отклонения', round(standardDeviationN, 3)])
    table_result.add_row(
        ['Интервальная оценка математического ожидания', '(' + str(round(x1N, 3)) + ', ' + str(round(x2N, 3)) + ')'])
    table_result.add_row(['Точечная оценка математического ожидания', round((x1N + x2N) / 2, 3)])
    print(table_result)
    print('\n')

    minN = m.ceil(min(selectionNormalDistribution) / 1000) * 1000
    maxN = m.floor(max(selectionNormalDistribution) / 1000) * 1000

    frequencyN = [i for i in range(minN, maxN, 200)]

    graphN = plt
    graphN.hist(selectionNormalDistribution, bins=frequencyN, edgecolor='white')
    graphN.title('Нормальный закон')
    graphN.xlabel('')
    graphN.ylabel('Частота')
    graphN.show()

    # логарифмически нормальное распределение
    selectionLogarithmicallyNormalDistribution = []
    beta = m.sqrt(m.log(1 + kv ** 2))
    alfa = m.log(mo - beta ** 2 / 2)
    for i in range(n):
        z2 = 0.0
        for y in range(12):
            z2 += r.uniform(0, 1)
        z2 -= 6
        y = alfa + z2 * beta
        x2 = m.exp(y)
        selectionLogarithmicallyNormalDistribution.append(x2)
    # selectionLogarithmicallyNormalDistribution = list(np.random.lognormal(mean=mo, size=n))

    averageL = stat.mean(selectionLogarithmicallyNormalDistribution)

    varianceL = stat.variance(selectionLogarithmicallyNormalDistribution)
    standardDeviationL = m.sqrt(varianceL)
    sigmaL = (1.96 * standardDeviationL) / (m.sqrt(n))
    x1L = averageL - sigmaL
    x2L = averageL + sigmaL

    table_resultL = pt()
    table_resultL.title = 'Логарифмически - нормальное распределение'
    table_resultL.field_names = ['Параметры оценки', 'Результат']
    table_resultL.add_row(['m', mo])
    table_resultL.add_row(['kv', kv])
    table_resultL.add_row(['n', n])
    table_resultL.add_row(['Оценка мат ожидания', round(averageL, 3)])
    table_resultL.add_row(['Оценка дисперсии', round(varianceL, 3)])
    table_resultL.add_row(['Оценка среднеквадратического отклонения', round(standardDeviationL, 3)])
    table_resultL.add_row(
        ['Интервальная оценка математического ожидания', '(' + str(round(x1L, 3)) + ', ' + str(round(x2L, 3)) + ')'])
    table_resultL.add_row(['Точечная оценка математического ожидания', round((x1L + x2L) / 2, 3)])
    print(table_resultL)

    minL = m.floor(min(selectionLogarithmicallyNormalDistribution) / 1000) * 1000
    maxL = m.ceil(max(selectionLogarithmicallyNormalDistribution) / 1000) * 1000

    frequencyL = [i for i in range(minL, maxL, 200)]

    plt.hist(selectionLogarithmicallyNormalDistribution, bins=frequencyL, edgecolor='white')
    plt.title('Логарифмически нормальное распределение')
    plt.xlabel('')
    plt.ylabel('Частота')
    plt.show()
