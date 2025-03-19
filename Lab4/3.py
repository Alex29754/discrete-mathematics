# Функция для кодирования текста с использованием алгоритма LZW
def lzw_encode(text):
    # Инициализация словаря с отдельными символами
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    # Переменные для хранения текущей строки и результата
    current_string = ""
    encoded_data = []

    # Проход по тексту
    for symbol in text:
        combined_string = current_string + symbol
        if combined_string in dictionary:
            current_string = combined_string
        else:
            # Добавляем код текущей строки в результат
            encoded_data.append(dictionary[current_string])
            # Добавляем новую строку в словарь
            dictionary[combined_string] = dict_size
            dict_size += 1
            current_string = symbol

    # Добавляем код последней строки
    if current_string:
        encoded_data.append(dictionary[current_string])

    return encoded_data


# Функция для вычисления количества бит после кодирования LZW
def calculate_lzw_bits(encoded_data):
    # Определяем максимальное значение в encoded_data
    max_value = max(encoded_data) if encoded_data else 0
    # Вычисляем количество бит, необходимых для хранения каждого числа
    bits_per_code = max_value.bit_length() if max_value > 0 else 1
    # Общее количество бит
    total_bits = len(encoded_data) * bits_per_code
    return total_bits


# Чтение текста из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Приведение текста к нижнему регистру и удаление лишних символов
text = text.lower()
allowed_chars = set('abcdefghijklmnopqrstuvwxyz ')
text = ''.join([char for char in text if char in allowed_chars])

# Кодирование текста с использованием LZW
encoded_data = lzw_encode(text)
lzw_bits = calculate_lzw_bits(encoded_data)

# Подсчёт количества бит для равномерных кодов и кодов Хаффмана
total_chars = len(text)
uniform_bits = total_chars * 6  # 6 бит на символ


huffman_bits = 63420  # Замените на значение из второго задания

# Вывод результатов
print(f"Количество бит (равномерные 6-битовые коды): {uniform_bits}")
print(f"Количество бит (коды Хаффмана): {huffman_bits}")
print(f"Количество бит (LZW): {lzw_bits}")

# Сравнение результатов
print("\nСравнение:")
print(f"LZW vs равномерные коды: {lzw_bits} бит vs {uniform_bits} бит")
print(f"LZW vs Хаффман: {lzw_bits} бит vs {huffman_bits} бит")