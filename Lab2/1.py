from itertools import permutations

word = "АБРАКАДАБРА"
unique_permutations = set(permutations(word, 4))

print("Количество различных 4-буквенных слов:", len(unique_permutations))
