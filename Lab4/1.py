from collections import Counter
import re

def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Приводим к нижнему регистру
    text = re.sub(r'[^a-z ]', '', text)  # Убираем все кроме букв и пробела
    return text

def frequency_analysis(text):
    letter_counts = Counter(text)
    total_letters = sum(letter_counts.values())

    pair_counts = Counter(text[i:i+2] for i in range(len(text)-1))
    total_pairs = sum(pair_counts.values())

    letter_freqs = {char: count / total_letters for char, count in letter_counts.items()}
    pair_freqs = {pair: count / total_pairs for pair, count in pair_counts.items()}

    return letter_freqs, pair_freqs

# Загрузка текста
filename = "text.txt"  # Имя файла с текстом
text = read_text(filename)

# Анализ частот
letter_freqs, pair_freqs = frequency_analysis(text)

# Вывод результатов
print("Частоты букв:")
for letter, freq in sorted(letter_freqs.items(), key=lambda x: -x[1]):
    print(f"{letter}: {freq:.4f}")

print("\nЧастоты пар букв:")
for pair, freq in sorted(pair_freqs.items(), key=lambda x: -x[1])[:10]:  # Топ-10 пар
    print(f"{pair}: {freq:.4f}")
