def annotate(minefield):
    if not minefield:
        return []

    rows = len(minefield)
    cols = len(minefield[0])

    if any(len(row) != cols for row in minefield):
        raise ValueError('The board is invalid with current input.')

    result = []
    for i in range(rows):

        curr_row = ''
        for j in range(cols):
            if minefield[i][j] == ' ':
                curr_row += count_mines(minefield, i, j)
            elif minefield[i][j] == '*':
                curr_row += minefield[i][j]
            else:
                raise ValueError('The board is invalid with current input.')

        minefield[i] = curr_row

    return minefield


def count_mines(minefield, row, col):
    x_axis = [0, 1, 0, -1, 1, -1, 1, -1]
    y_axis = [1, 0, -1, 0, -1, 1, 1, -1]

    mines_count = 0
    for k in range(8):
        x = row + x_axis[k]
        y = col + y_axis[k]
        if 0 <= x < len(minefield) and 0 <= y < len(minefield[0]) and minefield[x][y] == '*':
            mines_count += 1

    return str(mines_count) if mines_count > 0 else ' '
