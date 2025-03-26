import numpy as np


# 3. Вычисление минимального кодового расстояния
def hamming_distance(v1, v2):
    """Расчет кодового расстояния между двумя векторами"""
    return np.sum(v1 != v2)


def min_code_distance(G):
    """Нахождение минимального кодового расстояния"""
    codewords = [np.mod(np.dot(m, G), 2) for m in np.eye(G.shape[0], dtype=int)]
    min_distance = min(hamming_distance(c1, c2) for i, c1 in enumerate(codewords) for c2 in codewords[i + 1:])
    return min_distance


if __name__ == "__main__":
    G = np.array([[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]])  # Пример G

    min_dist = min_code_distance(G)
    print("Минимальное кодовое расстояние:", min_dist)
