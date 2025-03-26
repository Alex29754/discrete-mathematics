import math


def arithmetic_encode(symbols, probabilities, string):
    print(f"Символы: {symbols}")
    print(f"Вероятности: {probabilities}")
    print(f"Кодируемая строка: {string}\n")

    low = 0.0
    high = 1.0

    for char in string:
        range_ = high - low
        char_index = symbols.index(char)

        low_old, high_old = low, high
        high = low + range_ * sum(probabilities[:char_index + 1])
        low = low + range_ * sum(probabilities[:char_index])

        print(f"Символ: {char}")
        print(f"Диапазон перед изменением: [{low_old}, {high_old}]")
        print(f"Новый диапазон: [{low}, {high}]\n")

    encoded_value = (low + high) / 2
    print(f"Закодированное значение: {encoded_value}\n")

    # Определяем минимальное количество бит для точного представления
    num_bits = math.ceil(-math.log2(high - low))
    binary_encoded = format(int(encoded_value * (2 ** num_bits)), f'0{num_bits}b')

    print(f"Binary Encoded ({num_bits} bits): {binary_encoded}\n")
    return encoded_value, binary_encoded


# Пример использования
symbols = ['a', 'b', 'c', 'd', 'e', 'f']
probabilities = [0.05, 0.10, 0.05, 0.55, 0.15, 0.10]
encoded_value, binary_encoded = arithmetic_encode(symbols, probabilities, "eacdbf")