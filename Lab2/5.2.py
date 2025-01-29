def count_paths_with_restriction(n, k):
    if k > (n + 1) // 2:  # Невозможно пройти с таким ограничением
        return 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Стартовая точка

    for i in range(n + 1):
        for j in range(k + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]  # Горизонтальный шаг
            if i > 0 and j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # Вертикальный шаг, но не два подряд

    return dp[n][k]


# Размеры сетки
n, k = 18, 15

# Количество кратчайших путей с ограничением
paths_with_restriction = count_paths_with_restriction(n, k)

print("Кратчайших путей с ограничением (без двух подряд вертикальных шагов):", paths_with_restriction)
