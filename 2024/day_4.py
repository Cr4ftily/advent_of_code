N = (0, 1)
NE = (1, 1)
E = (1, 0)
SE = (1, -1)
S = (0, -1)
SW = (-1, -1)
W = (-1, 0)
NW = (-1, 1)

DIRECTIONS = [N, NE, E, SE, S, SW, W, NW]

def add_d(origin, direction):
    return (origin[0] + direction[0], origin[1] + direction[1])


def find_xmas(input, origin, dir, str = "X"):
    (x, y) = add_d(origin, dir)
    if x < 0 or y < 0 or len(str) > 3:
        return "XMAS" in str[:4]
    try:
        str = str + input[x][y]
    except IndexError:
        return "XMAS" in str[:4]
    return find_xmas(input, (x, y), dir, str)


def get(data, coordinates):
    (x, y) = coordinates
    return data[x][y]

def find_x_mas(input, origin):
    d1, d2 = '', ''
    try:
        d1 = get(input, add_d(origin, NE)) + get(input, add_d(origin, SW))
        d2 = get(input, add_d(origin, NW)) + get(input, add_d(origin, SE))
    except IndexError:
        return 0
    return 'M' in d1 and 'S' in d1 and 'M' in d2 and 'S' in d2

def xmas(input):
    s, s2 = 0, 0
    for i, row in enumerate(input):
        for j, column in enumerate(row):
            if column == 'X':
                for dir in DIRECTIONS:
                    s += find_xmas(input, (i, j), dir)
            if column == 'A':
                s2 += find_x_mas(input, (i, j))
    return s, s2

with open('2024/input_4.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line.strip('\n'))
    print(xmas(input))