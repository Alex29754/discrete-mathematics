import heapq
from collections import defaultdict, Counter

def build_huffman_tree(freq):
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
    return heap[0][1:]

def huffman_encode(data, codes):
    return ''.join(codes[char] for char in data)

def huffman_decode(encoded, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded = []
    for bit in encoded:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ""
    return ''.join(decoded)

# Пример использования
freq = {'A': 2, 'B': 3, 'C': 7, 'D': 9, 'E': 18, 'F': 20, 'G': 41}
huffman_tree = build_huffman_tree(freq)
codes = {char: code for char, code in huffman_tree}
encoded = huffman_encode("ABCDEFG", codes)
decoded = huffman_decode(encoded, codes)

print("Encoded:", encoded)
print("Decoded:", decoded)