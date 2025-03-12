def hamming_distance(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))

def find_error(code, codes):
    for i, c in enumerate(codes):
        if hamming_distance(code, c) == 1:
            return i
    return -1

def correct_error(code, codes):
    for c in codes:
        if hamming_distance(code, c) == 1:
            return c
    return code

# Пример использования
letters = "nonperdxx"
codes_distance_2 = ["000", "011", "101", "110"]
codes_distance_3 = ["0000", "0111", "1011", "1100"]

# Демонстрация поиска ошибки
error_code = "001"
error_index = find_error(error_code, codes_distance_2)
print("Error found at index:", error_index)

# Демонстрация исправления ошибки
corrected_code = correct_error(error_code, codes_distance_3)
print("Corrected code:", corrected_code)