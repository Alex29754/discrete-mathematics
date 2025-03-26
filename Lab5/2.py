import numpy as np


# 2. Кодирование сообщения
def encode_message(G, message):
    """Кодирование сообщения"""
    return np.mod(np.dot(message, G), 2)


if __name__ == "__main__":
    n = 31  # Общая длина кода
    generator_poly = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]  # Порождающий многочлен
    G = np.array([[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]])  # Пример G

    message = np.array([1, 0, 1, 1])  # Пример сообщения
    encoded = encode_message(G, message)
    print("Закодированное сообщение:")
    print(encoded)
