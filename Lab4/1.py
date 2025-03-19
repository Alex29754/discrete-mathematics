from collections import defaultdict, Counter
import string

# Чтение текста из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Приведение текста к нижнему регистру для упрощения анализа
text = text.lower()

# Удаление всех символов, кроме букв и пробелов
allowed_chars = string.ascii_lowercase + ' '
text = ''.join([char for char in text if char in allowed_chars])

# Статистика по частоте букв
letter_frequency = Counter(text)

# Статистика по частоте пар букв
pair_frequency = defaultdict(int)
for i in range(len(text) - 1):
    pair = text[i:i+2]
    pair_frequency[pair] += 1

# Вывод результатов
print("Частота букв:")
for letter, freq in letter_frequency.items():
    print(f"{letter}: {freq}")

print("\nЧастота пар букв:")
for pair, freq in pair_frequency.items():
    print(f"{pair}: {freq}")