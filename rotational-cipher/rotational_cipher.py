def rotate(text, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    cipher = [alphabets[(index + key) % 26] for index in range(26)]

    alphabets += alphabets.upper()
    cipher.extend([char.upper() for char in cipher])

    result = [cipher[alphabets.index(char)] if char in alphabets else char for char in text]

    return ''.join(result)
