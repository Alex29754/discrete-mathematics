from math import comb

# Размеры сетки
n, k = 18, 15

# Количество кратчайших путей
paths_no_restrictions = comb(n + k, k)

print("Кратчайших путей без ограничений:", paths_no_restrictions)
