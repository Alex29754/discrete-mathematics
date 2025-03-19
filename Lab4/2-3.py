import heapq
from collections import Counter
import math


# Функция для построения кодов Хаффмана
def build_huffman_codes(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = dict(heapq.heappop(heap)[1:])
    return huffman_codes


# Функция для кодирования текста с использованием кодов Хаффмана
def huffman_encode(text, codes):
    return ''.join([codes[char] for char in text])


# Функция для расчёта количества информации по формуле Шеннона
def shannon_entropy(freq, total):
    return -sum((f / total) * math.log2(f / total) for f in freq.values())


# Чтение текста из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Приведение текста к нижнему регистру и удаление лишних символов
text = text.lower()
allowed_chars = set('abcdefghijklmnopqrstuvwxyz ')
text = ''.join([char for char in text if char in allowed_chars])

# Подсчёт количественной частоты символов (первая задача)
letter_frequency = Counter(text)
total_chars = len(text)

# Вывод результатов первой задачи
print("Частота символов:")
for char, freq in letter_frequency.items():
    print(f"{char}: {freq}")

# Построение кодов Хаффмана (вторая задача)
huffman_codes = build_huffman_codes(letter_frequency)

# Кодирование текста с использованием кодов Хаффмана
encoded_text = huffman_encode(text, huffman_codes)
huffman_bits = len(encoded_text)

# Кодирование текста с использованием равномерных 6-битовых кодов
uniform_bits = total_chars * 6

# Расчёт количества информации по формуле Шеннона
entropy = shannon_entropy(letter_frequency, total_chars)
shannon_bits = entropy * total_chars

# Вывод результатов второй задачи
print("\nКоды Хаффмана:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

print(f"\nЗакодированный текст (Хаффман): {encoded_text}")
print(f"Количество бит (Хаффман): {huffman_bits}")

print(f"\nКоличество бит (равномерные 6-битовые коды): {uniform_bits}")

print(f"\nЭнтропия по Шеннону: {entropy:.4f} бит/символ")
print(f"Количество информации по Шеннону: {shannon_bits:.4f} бит")

# Сравнение результатов
print("\nСравнение:")
print(f"Хаффман vs равномерные коды: {huffman_bits} бит vs {uniform_bits} бит")
print(f"Хаффман vs Шеннон: {huffman_bits} бит vs {shannon_bits:.4f} бит")
