def count_restricted_paths(m, n):
    right = [0] * (n + 1)
    up = [0] * (n + 1)
    right[0] = 1  # Начальная клетка

    for _ in range(m + 1):
        new_right = [0] * (n + 1)
        new_up = [0] * (n + 1)
        for j in range(n + 1):
            if j == 0:
                new_right[j] = right[j] + up[j]
            else:
                new_right[j] = right[j] + up[j]
                new_up[j] = new_right[j - 1]
        right, up = new_right, new_up

    return right[n] + up[n]

# Для сетки 18x15 клеток (m=18, n=15)
print(count_restricted_paths(18, 15))