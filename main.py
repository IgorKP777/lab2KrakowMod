import random
import math
import numpy as np
import statistics as stat
from matplotlib import pyplot as plt
from prettytable import PrettyTable as pt


def log_norm():
    mo = 5
    diss = 1
    n = 1000
    beta = math.sqrt(math.log(1 + (diss / mo ** 2)))
    alfa = math.log(mo) - ((beta ** 2) / 2)
    # list = []
    # for i in range(n):
    #     z = 0
    #     for y in range(12):
    #         z += r.uniform(0, 1)
    #     z -= 6
    #     y = mo + beta * z
    #     x = math.exp(y)
    #     list.append(x)
    lt = list(np.random.normal(loc=mo, size=n))
    mean = stat.mean(lt)
    variance = stat.variance(lt)
    standard_deviation = math.sqrt(variance)
    table_result = pt()
    table_result.title = 'Результаты'
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
    # min1 = math.ceil(min(lt) / 1000) * 1000
    # max1 = math.floor(max(lt) / 1000) * 1000
    min1 = min(lt)
    max1 = max(lt)
    frequency = [round(i, 3) for i in np.arange(min1, max1, (min1 + max1) / 40)]
    graphN.hist(x=lt, bins=frequency, edgecolor='white')
    graphN.title('Нормальный закон')
    graphN.xlabel('')
    graphN.ylabel('Частота')
    graphN.show()


if __name__ == '__main__':

    # log_norm()

    n = 1000
    mo = 5
    kv = 1

    # нормальное распределение
    selectionNormalDistribution = list(np.random.normal(loc=mo, scale=1000, size=n))
    averageN = stat.mean(selectionNormalDistribution)
    varianceN = stat.variance(selectionNormalDistribution)

    standardDeviationN = math.sqrt(varianceN)

    sigmaN = (1.96 * standardDeviationN) / (math.sqrt(n))
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

    # minN = math.ceil(min(selectionNormalDistribution) / 1000) * 1000
    # maxN = math.floor(max(selectionNormalDistribution) / 1000) * 1000
    minN = min(selectionNormalDistribution)
    maxN = max(selectionNormalDistribution)

    frequencyN = [round(i, 3) for i in np.arange(minN, maxN, (minN + maxN) / 40)]

    graphN = plt
    graphN.hist(selectionNormalDistribution, bins=frequencyN, edgecolor='white')
    graphN.title('Нормальный закон')
    graphN.xlabel('')
    graphN.ylabel('Частота')
    graphN.show()

    # логарифмически нормальное распределение
    selectionLogarithmicallyNormalDistribution = []
    beta = math.sqrt(math.log(1 + kv ** 2))
    alfa = math.log(mo - beta ** 2 / 2)
    for i in range(n):
        z2 = 0.0
        for y in range(12):
            z2 += random.uniform(0, 1)
        z2 -= 6
        y = alfa + z2 * beta
        x2 = math.exp(y)
        selectionLogarithmicallyNormalDistribution.append(x2)

    averageL = stat.mean(selectionLogarithmicallyNormalDistribution)

    varianceL = stat.variance(selectionLogarithmicallyNormalDistribution)
    standardDeviationL = math.sqrt(varianceL)
    sigmaL = (1.96 * standardDeviationL) / (math.sqrt(n))
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

    minL = math.floor(min(selectionLogarithmicallyNormalDistribution) / 1000) * 1000
    maxL = math.ceil(max(selectionLogarithmicallyNormalDistribution) / 1000) * 1000

    frequencyL = [i for i in range(minL, maxL, 200)]

    plt.hist(selectionLogarithmicallyNormalDistribution, bins=frequencyL, edgecolor='white')
    plt.title('Логарифмически нормальное распределение')
    plt.xlabel('')
    plt.ylabel('Частота')
    plt.show()
