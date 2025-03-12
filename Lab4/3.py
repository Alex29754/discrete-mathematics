import heapq
import re
from collections import Counter

# Функция для чтения текста из файла
def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Приводим к нижнему регистру
    text = re.sub(r'[^a-z ]', '', text)  # Оставляем только латинские буквы и пробел
    return text

# 1. Частотный анализ
def frequency_analysis(text):
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())

    pair_counts = Counter(text[i:i+2] for i in range(len(text)-1))
    total_pairs = sum(pair_counts.values())

    letter_freqs = {char: count / total_letters for char, count in letter_counts.items()}
    pair_freqs = {pair: count / total_pairs for pair, count in pair_counts.items()}

    return letter_freqs, pair_freqs

# 2. Кодирование Хаффмана
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

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

def generate_huffman_codes(node, prefix="", codebook={}):
    if node:
        if node.char:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# 3. Кодирование LZW
def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}  # Инициализируем словарь ASCII
    next_code = 256
    w = ""
    compressed = []

    for char in text:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = char

    if w:
        compressed.append(dictionary[w])  # Записываем оставшуюся строку

    return compressed

# --- Основная часть программы ---
filename = "text.txt"  # Укажи путь к файлу с текстом
text = read_text(filename)

# 1. Анализ частот
letter_freqs, pair_freqs = frequency_analysis(text)

# 2. Кодирование Хаффмана
huffman_tree = build_huffman_tree(letter_freqs)
huffman_codes = generate_huffman_codes(huffman_tree)
encoded_huffman = encode_text(text, huffman_codes)

# 3. Кодирование LZW
encoded_lzw = lzw_compress(text)

# --- Вывод результатов ---
print("\nЧастоты букв:")
for letter, freq in sorted(letter_freqs.items(), key=lambda x: -x[1]):
    print(f"{letter}: {freq:.4f}")

print("\nЧастоты пар букв:")
for pair, freq in sorted(pair_freqs.items(), key=lambda x: -x[1])[:10]:  # Топ-10 пар
    print(f"{pair}: {freq:.4f}")

print("\nКоды Хаффмана:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

print(f"\nЗакодированный текст Хаффмана (первые 100 бит): {encoded_huffman[:100]}")

print("\nЗакодированный текст LZW (первые 20 кодов):", encoded_lzw[:20])
print(f"Длина закодированного текста LZW: {len(encoded_lzw)}")
