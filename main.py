import random as r
import math as m
import numpy as np
import statistics as stat
from matplotlib import pyplot as plt


def normal():
    pass


def log_normal():
    pass


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
    print('----- Нормальный закон -----')
    print('m =', mo, '(мат ожидание)')
    print('kv =', kv, '(коэффициент вариации)')
    print('n =', n, '(размер выборки)')
    print('Оценка мат ожидания\n', round(averageN, 3), sep='')
    print('Оценка дисперсии\n', round(varianceN, 3), sep='')
    print('Оценка среднеквадратического отклонения\n', round(standardDeviationN, 3), sep='')
    print('Интервальная оценка математического ожидания\n', '(', round(x1N, 3), ', ', round(x2N, 3), ')', sep='')
    print('Точечная оценка математического ожидания\n', round((x1N + x2N) / 2, 3), sep='')
    print('\n', '\n')

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
    print('----- Логарифмически - нормальное распределение -----')
    print('m =', mo, 'мат ожидание')
    print('kv =', kv, 'коэффициент вариации')
    print('n =', n, 'размер выборки')
    print('оценка мат ожидания\n', round(averageL, 3))
    print('оценка дисперсии\n', round(varianceL, 3))
    print('оценка среднеквадратического отклонения\n', round(standardDeviationL, 3))
    print('интервальная оценка математического ожидания\n', '(', round(x1L, 3), ',', round(x2L, 3), ')')
    print('точечная оценка математического ожидания\n', round((x1L + x2L) / 2, 3))

    minL = m.floor(min(selectionLogarithmicallyNormalDistribution) / 1000) * 1000
    maxL = m.ceil(max(selectionLogarithmicallyNormalDistribution) / 1000) * 1000

    frequencyL = [i for i in range(minL, maxL, 200)]

    plt.hist(selectionLogarithmicallyNormalDistribution, bins=frequencyL, edgecolor='white')
    plt.title('Логарифмически нормальное распределение')
    plt.xlabel('')
    plt.ylabel('Частота')
    plt.show()
