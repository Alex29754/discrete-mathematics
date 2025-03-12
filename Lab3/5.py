def arithmetic_encode(symbols, probabilities, string):
    low = 0.0
    high = 1.0
    for char in string:
        range_ = high - low
        high = low + range_ * sum(probabilities[:symbols.index(char) + 1])
        low = low + range_ * sum(probabilities[:symbols.index(char)])
    return (low + high) / 2

# Пример использования
symbols = ['a', 'b', 'c', 'd', 'e', 'f']
probabilities = [0.05, 0.10, 0.05, 0.55, 0.15, 0.10]
encoded_value = arithmetic_encode(symbols, probabilities, "eacdbf")
binary_encoded = format(int(encoded_value * (2**32)), '032b')
print("Binary Encoded:", binary_encoded)