# link to problem: https://www.hackerrank.com/challenges/encryption/problem

import math

def getGrid(col, string):
    grid_system = []
    counter = 0
    letters_on_row = []
    for l in string:
        letters_on_row.append(l)
        counter += 1
        if counter == col:
            counter = 0
            grid_system.append(letters_on_row)
            letters_on_row = []
    if len(letters_on_row) > 0:
        grid_system.append(letters_on_row + ['']*(col-len(letters_on_row)))
    return grid_system


def encryption(string_to_encrypt):
    length = len(string_to_encrypt)
    root = math.sqrt(length)
    row, col = math.floor(root), math.ceil(root)
    if row * col < length:
        if row < col:
            row += 1
        else:
            col += 1
    grid = getGrid(col, string_to_encrypt)
    code = []
    for c in range(col):
        word = ''
        for r in range(row):
            word += grid[r][c] if grid[r][c] else ''
        code.append(word)

    return ' '.join(code)


s = input()
print(encryption(s.replace(' ', '')))
