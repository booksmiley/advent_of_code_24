import numpy as np

lines = []
with open('./input_04.txt', 'r') as f:
    for line in f:
        line = np.array([c for c in line.strip()])
        lines.append(line)
lines = np.array(lines)

template = 'XMAS'


h = len(lines)
w = len(lines[0])


def search_square(s, i, j):
    count = 0
    if j + 3 < w:
        h_line = s[i][j] + s[i][j+1] + s[i][j+2] + s[i][j+3]
        if h_line == template:
            count += 1
    if i + 3 < h:
        v_line = s[i][j] + s[i+1][j] + s[i+2][j] + s[i+3][j]
        if v_line == template:
            count += 1

    if i + 3 < h and j + 3 < w:
        d_line = s[i][j] + s[i+1][j+1] + s[i+2][j+2] + s[i+3][j+3]
        if d_line == template:
            count += 1

    if j >= 3:
        r_h_line = s[i][j] + s[i][j-1] + s[i][j-2] + s[i][j-3]
        if r_h_line == template:
            count += 1

    if i >= 3:
        r_v_line = s[i][j] + s[i-1][j] + s[i-2][j] + s[i-3][j]
        if r_v_line == template:
            count += 1

    if i >= 3 and j >= 3:
        r_d_line = s[i][j] + s[i-1][j-1] + s[i-2][j-2] + s[i-3][j-3]
        if r_d_line == template:
            count += 1

    if i >= 3 and j + 3 < w:
        od_line = s[i][j] + s[i-1][j+1] + s[i-2][j+2] + s[i-3][j+3]
        if od_line == template:
            count += 1

    if i + 3 < h and j >= 3:
        r_od_line = s[i][j] + s[i+1][j-1] + s[i+2][j-2] + s[i+3][j-3]
        if r_od_line == template:
            count += 1
    return count


def search_x_square(s, i, j):
    square = s[i: i + 3, j: j + 3]
    if square.shape != (3, 3):
        return 0
    if square[0][0] + square[1][1] + square[2][2] in templates and square[0][2] + square[1][1] + square[2][0] in templates:
        return 1
    return 0


count = 0
for i in range(h):
    for j in range(w):
        count += search_square(lines, i, j)

print(count)
