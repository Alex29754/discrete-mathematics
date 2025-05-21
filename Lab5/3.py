import numpy as np

class CyclicCode:
    def __init__(self, n, k, generator_poly):
        self.n = n
        self.k = k
        self.r = n - k
        self.generator_poly = generator_poly
        self.g = [int(bit) for bit in generator_poly]
        self.g_degree = len(self.g) - 1
        assert self.g_degree == self.r, "Степень порождающего многочлена должна быть равна n-k"
        self.G = self.build_systematic_generator_matrix()
        self.d_min = self.calculate_min_distance()
        self.syndrome_table = self.build_syndrome_table()

    def poly_div(self, dividend, divisor):
        dividend = np.array(dividend, dtype=int)
        divisor = np.array(divisor, dtype=int)
        dividend = np.trim_zeros(dividend, 'f')
        divisor = np.trim_zeros(divisor, 'f')

        if len(dividend) < len(divisor):
            return dividend.copy()

        remainder = dividend.copy()
        for i in range(len(dividend) - len(divisor) + 1):
            if remainder[i] == 1:
                remainder[i:i + len(divisor)] ^= divisor

        remainder = np.trim_zeros(remainder, 'f')
        return remainder

    def build_systematic_generator_matrix(self):
        I_k = np.eye(self.k, dtype=int)
        C = []

        for i in range(self.k):
            x_power = np.zeros(self.k, dtype=int)
            x_power[i] = 1
            shifted = np.concatenate([x_power, np.zeros(self.r, dtype=int)])
            remainder = self.poly_div(shifted, self.g)
            if len(remainder) < self.r:
                remainder = np.concatenate([np.zeros(self.r - len(remainder), dtype=int), remainder])
            C.append(remainder)

        C = np.array(C, dtype=int)
        G = np.hstack([I_k, C])
        return G

    def encode(self, message):
        if len(message) != self.k:
            raise ValueError(f"Длина сообщения должна быть {self.k} бит")

        remainder = self.poly_div(np.concatenate([message, np.zeros(self.r, dtype=int)]), self.g)
        if len(remainder) < self.r:
            remainder = np.concatenate([np.zeros(self.r - len(remainder), dtype=int), remainder])
        return np.concatenate([message, remainder])

    def calculate_min_distance(self):
        min_weight = sum(self.g)

        for i in range(self.k):
            row = self.G[i]
            weight = sum(row)
            if 0 < weight < min_weight:
                min_weight = weight

        for i in range(self.k):
            for j in range(i + 1, self.k):
                combined = (self.G[i] + self.G[j]) % 2
                weight = sum(combined)
                if 0 < weight < min_weight:
                    min_weight = weight

        for i in range(self.k):
            for j in range(i + 1, self.k):
                for m in range(j + 1, self.k):
                    combined = (self.G[i] + self.G[j] + self.G[m]) % 2
                    weight = sum(combined)
                    if 0 < weight < min_weight:
                        min_weight = weight

        return min_weight

    def calculate_syndrome(self, received):
        remainder = self.poly_div(received, self.g)
        if len(remainder) < self.r:
            remainder = np.concatenate([np.zeros(self.r - len(remainder), dtype=int), remainder])
        return remainder

    def build_syndrome_table(self):
        syndrome_table = {}
        for i in range(self.n):
            error = np.zeros(self.n, dtype=int)
            error[i] = 1
            syndrome = tuple(self.calculate_syndrome(error))
            syndrome_table[syndrome] = error
        return syndrome_table

    def correct_errors(self, received):
        syndrome = self.calculate_syndrome(received)
        correction = self.syndrome_table.get(tuple(syndrome), None)
        if correction is not None:
            corrected = (received + correction) % 2
            return corrected, True, syndrome
        return received, False, syndrome

    def decode(self, received):
        if len(received) != self.n:
            raise ValueError(f"Длина принятого слова должна быть {self.n} бит")

        syndrome = self.calculate_syndrome(received)
        error_detected = np.any(syndrome != 0)
        corrected, corrected_flag, _ = self.correct_errors(received)
        return {
            'error_detected': error_detected,
            'corrected': corrected_flag,
            'syndrome': syndrome,
            'corrected_word': corrected if corrected_flag else received
        }

    def get_capabilities(self):
        detect = self.d_min - 1
        correct = (self.d_min - 1) // 2
        return detect, correct

    def generate_error_examples(self):
        message = np.zeros(self.k, dtype=int)
        message[0] = 1
        codeword = self.encode(message)

        print("\n3. Примеры, иллюстрирующие свойства кода:")

        for idx, error_positions in enumerate([[5], [5, 10], [5, 10, 15]], 1):
            error = np.zeros(self.n, dtype=int)
            for pos in error_positions:
                error[pos] = 1
            received = (codeword + error) % 2
            result = self.decode(received)

            print(f"\nПример {idx}: Ошибка в позиции(ях) {error_positions}")
            print(f"Кодовое слово:         {codeword}")
            print(f"Вектор ошибки:         {error}")
            print(f"Принятое слово:        {received}")
            print(f"Синдром:               {result['syndrome']}")
            print(f"Ошибка обнаружена:     {result['error_detected']}")
            print(f"Ошибка исправлена:     {result['corrected']}")
            if result['corrected']:
                print(f"Исправленное слово:    {result['corrected_word']}")
# Параметры кода
n = 31
k = 16
generator_poly = '1000111110101111'

# Создаем экземпляр кода
code = CyclicCode(n, k, generator_poly)

# 1. Порождающая матрица
print("1. Порождающая матрица G:")
print(code.G)

# 2. Характеристики кода
d_min = code.d_min
detect, correct = code.get_capabilities()
print(f"\n2. Характеристики кода:")
print(f"Минимальное расстояние кода: d_min = {d_min}")
print(f"Кратность гарантированно обнаруживаемых ошибок: {detect}")
print(f"Кратность гарантированно исправляемых ошибок: {correct}")

# 3. Примеры иллюстрирующие свойства кода
code.generate_error_examples()
# Моя программа реализует циклический (n, k)-код с заданным порождающим многочленом. Она строит порождающую матрицу, кодирует сообщение,
# вычисляет минимальное расстояние кода, проверяет наличие ошибок по синдрому и исправляет ошибки с помощью таблицы синдромов.
# Синдром получается как остаток от деления принятого слова на порождающий многочлен. Если синдром не ноль, то ошибка есть.
# Если синдром есть в таблице, мы знаем точный вектор ошибки и можем исправить принятое слово.