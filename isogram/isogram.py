def is_isogram(string):
    word = string.lower().replace(" ", "").replace("-", "")
    return len(set(word)) == len(word)
