def hamming_encode(data):
    print(f"Исходные данные: {data}")
    n = len(data)
    r = 0
    while (2 ** r) < (n + r + 1):
        r += 1

    print(f"Число контрольных битов: {r}")

    encoded = ['0'] * (n + r)
    j = 0
    for i in range(1, len(encoded) + 1):
        if i & (i - 1) == 0:
            continue
        encoded[i - 1] = data[j]
        j += 1

    print(f"Данные с зарезервированными позициями под контрольные биты: {''.join(encoded)}")

    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, len(encoded) + 1):
            if j & pos:
                parity ^= int(encoded[j - 1])
        encoded[pos - 1] = str(parity)
        print(f"Контрольный бит на позиции {pos}: {parity}")

    result = ''.join(encoded)
    print(f"Закодированные данные: {result}\n")
    return result


def hamming_decode(encoded):
    print(f"Полученные данные для декодирования: {encoded}")
    n = len(encoded)
    r = 0
    while (2 ** r) < n:
        r += 1

    error_pos = 0
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= int(encoded[j - 1])
        if parity != 0:
            error_pos += pos
        print(f"Проверка контрольного бита {pos}: {'ошибка' if parity else 'OK'}")

    if error_pos:
        print(f"Обнаружена ошибка в позиции: {error_pos}")
        encoded = list(encoded)
        encoded[error_pos - 1] = '1' if encoded[error_pos - 1] == '0' else '0'
        encoded = ''.join(encoded)
        print(f"Исправленные данные: {encoded}")
    else:
        print("Ошибок не обнаружено.")

    decoded = []
    for i in range(1, n + 1):
        if i & (i - 1) != 0:
            decoded.append(encoded[i - 1])
    result = ''.join(decoded)
    print(f"Декодированные данные: {result}\n")
    return result


# Пример использования
data = "abstract"
binary_data = ''.join(format(ord(char), '08b') for char in data)
block1 = binary_data[:32]
block2 = binary_data[32:64]

encoded_block1 = hamming_encode(block1)
encoded_block2 = hamming_encode(block2)

# Имитация ошибок
encoded_block1 = encoded_block1[:4] + ('1' if encoded_block1[4] == '0' else '0') + encoded_block1[5:]
encoded_block2 = encoded_block2[:20] + ('1' if encoded_block2[20] == '0' else '0') + encoded_block2[21:]

print("--- Декодирование ---")
decoded_block1 = hamming_decode(encoded_block1)
decoded_block2 = hamming_decode(encoded_block2)

print("Decoded Block 1:", decoded_block1)
print("Decoded Block 2:", decoded_block2)
