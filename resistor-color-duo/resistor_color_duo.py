COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']


def value(colors):
    result = 0
    for i in range(2):
        result = result * 10 + COLORS.index(colors[i])

    return result
