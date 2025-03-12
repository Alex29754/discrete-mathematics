import heapq
import re
from collections import Counter

# Функция для чтения текста из файла
def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Приводим к нижнему регистру
    text = re.sub(r'[^a-z ]', '', text)  # Убираем все кроме букв и пробела
    return text

# Функция для анализа частот букв и пар букв
def frequency_analysis(text):
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())

    pair_counts = Counter(text[i:i+2] for i in range(len(text)-1))
    total_pairs = sum(pair_counts.values())

    letter_freqs = {char: count / total_letters for char, count in letter_counts.items()}
    pair_freqs = {pair: count / total_pairs for pair, count in pair_counts.items()}

    return letter_freqs, pair_freqs

# Класс узла для дерева Хаффмана
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Функция для построения дерева Хаффмана
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Функция для генерации кодов Хаффмана
def generate_huffman_codes(node, prefix="", codebook={}):
    if node:
        if node.char:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

# Функция для кодирования текста с использованием кодов Хаффмана
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# --- Основная часть программы ---
filename = "text.txt"  # Укажи путь к файлу с текстом
text = read_text(filename)

# 1. Анализ частот
letter_freqs, pair_freqs = frequency_analysis(text)

# 2. Построение кодов Хаффмана
huffman_tree = build_huffman_tree(letter_freqs)
huffman_codes = generate_huffman_codes(huffman_tree)

# Кодирование текста
encoded_text = encode_text(text, huffman_codes)

# Вывод результатов
print("\nЧастоты букв:")
for letter, freq in sorted(letter_freqs.items(), key=lambda x: -x[1]):
    print(f"{letter}: {freq:.4f}")

print("\nЧастоты пар букв:")
for pair, freq in sorted(pair_freqs.items(), key=lambda x: -x[1])[:10]:  # Топ-10 пар
    print(f"{pair}: {freq:.4f}")

print("\nКоды Хаффмана:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

print(f"\nЗакодированный текст (первые 100 бит): {encoded_text[:100]}")
