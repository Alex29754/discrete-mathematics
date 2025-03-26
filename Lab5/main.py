import numpy as np
import itertools


# 1. Построение порождающей матрицы
def generate_matrix(generator_poly, n, t):
    """Формирует порождающую матрицу"""
    k = len(generator_poly)
    G = np.zeros((t, n), dtype=int)
    for i in range(t):
        G[i, i:i + k] = generator_poly
    return G


# 2. Кодирование сообщений
def encode_message(G, message):
    """Кодирование сообщения"""
    return np.mod(np.dot(message, G), 2)


# 3. Нахождение минимального кодового расстояния
def hamming_distance(v1, v2):
    """Расчет кодового расстояния между двумя векторами"""
    return np.sum(v1 != v2)


def min_code_distance(G):
    """Нахождение минимального кодового расстояния"""
    codewords = [np.mod(np.dot(m, G), 2) for m in np.eye(G.shape[0], dtype=int)]
    min_distance = min(hamming_distance(c1, c2) for i, c1 in enumerate(codewords) for c2 in codewords[i + 1:])
    return min_distance


# 4. Определение исправляемых и обнаруживаемых ошибок
def error_correction_characteristics(d):
    """Определяет характеристики кода"""
    t_correct = (d - 1) // 2  # Число исправляемых ошибок
    t_detect = d - 1  # Число обнаруживаемых ошибок
    return t_correct, t_detect


# 5. Поиск ошибки, которую код может обнаружить, но не исправить
def find_uncorrectable_error(G):
    """Ищет ошибку, которую код обнаружит, но не исправит"""
    t = G.shape[0]
    error_vectors = [np.array(e) for e in itertools.product([0, 1], repeat=G.shape[1]) if
                     sum(e) > (min_code_distance(G) // 2)]
    for e in error_vectors:
        syndrome = np.mod(np.dot(e, G.T), 2)
        if np.any(syndrome):
            return e  # Возвращает первый найденный необнаружимый вектор
    return None


if __name__ == "__main__":
    n = 31  # Общая длина кода
    t = 16  # Число информационных символов
    generator_poly = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]  # Порождающий многочлен

    # 1. Построение порождающей матрицы
    G = generate_matrix(generator_poly, n, t)
    print("Порождающая матрица:")
    print(G)

    # 2. Кодирование примера сообщения
    message = np.random.randint(0, 2, size=(t,))
    encoded = encode_message(G, message)
    print("Закодированное сообщение:", encoded)

    # 3. Минимальное кодовое расстояние
    d_min = min_code_distance(G)
    print("Минимальное кодовое расстояние:", d_min)

    # 4. Определение характеристик исправления ошибок
    t_correct, t_detect = error_correction_characteristics(d_min)
    print(f"Гарантированно исправляемые ошибки: {t_correct}")
    print(f"Гарантированно обнаруживаемые ошибки: {t_detect}")

    # 5. Поиск ошибки, которую код может обнаружить, но не исправить
    error_vector = find_uncorrectable_error(G)
    print("Ошибка, которую код может обнаружить, но не исправить:", error_vector)