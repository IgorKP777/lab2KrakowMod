import math
import numpy as np
import statistics as stat
from matplotlib import pyplot as plt
from prettytable import PrettyTable as pt


def norm():
    mo = 5
    diss = 1
    n = 1000
    lt = list(np.random.normal(loc=mo, scale=diss, size=n))
    averageN = stat.mean(lt)
    varianceN = stat.variance(lt)
    standardDeviationN = math.sqrt(varianceN)
    sigmaN = (1.96 * standardDeviationN) / (math.sqrt(n))
    x1N = averageN - sigmaN
    x2N = averageN + sigmaN
    table_result = pt()
    table_result.title = 'Нормальный закон'
    table_result.field_names = ['Параметры оценки', 'Результат']
    table_result.add_row(['Оценка мат ожидания', round(averageN, 3)])
    table_result.add_row(['Оценка дисперсии', round(varianceN, 3)])
    table_result.add_row(['Оценка среднеквадратического отклонения', round(standardDeviationN, 3)])
    table_result.add_row(
        ['Интервальная оценка математического ожидания', '(' + str(round(x1N, 3)) + ', ' + str(round(x2N, 3)) + ')'])
    table_result.add_row(['Точечная оценка математического ожидания', round((x1N + x2N) / 2, 3)])
    print(table_result)
    min1 = min(lt)
    max1 = max(lt)
    frequency = [round(i, 3) for i in np.arange(min1, max1, (min1 + max1) / 40)]
    graphN = plt
    graphN.hist(x=lt, bins=frequency, edgecolor='white')
    graphN.title('Нормальный закон')
    graphN.xlabel('')
    graphN.ylabel('Частота')
    graphN.show()