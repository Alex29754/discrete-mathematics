def rle_encode(data):
    encoded = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        if count > 1:
            encoded.append(str(count))
            encoded.append(data[i])
        else:
            encoded.append('0')
            encoded.append(data[i])
        i += 1
    return ''.join(encoded)

# Пример использования
data = "aaaaadggggggggggggghtyiklooooop"
encoded_data = rle_encode(data)
print("Encoded Data:", encoded_data)