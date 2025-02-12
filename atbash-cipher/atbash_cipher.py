from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(text):
    text = ''.join(a.lower() for a in text if a.isalnum())
    text = text.translate(ENCODING)
    return ' '.join(text[i:i + 5] for i in range(0, len(text), 5))


def decode(text):
    return text.translate(ENCODING).replace(" ", "")
