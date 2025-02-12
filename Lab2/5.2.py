def count_paths(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] += dp[i-1][j]  # Горизонтальный шаг
            if j > 0:
                if i == 0:
                    dp[i][j] += dp[i][j-1]  # Вертикальный шаг, если это первый ряд
                else:
                    dp[i][j] += dp[i][j-1]  # Вертикальный шаг, если предыдущий шаг не был вертикальным

    return dp[m][n]

m = 18
n = 15
print(count_paths(m, n))