from icecream import ic

steps = 3
shifts = [
    {'x': 1, 'y': 1}, # se
    {'x': -1, 'y': -1}, # nw
    {'x': -1, 'y': 1}, # sw
    {'x': 1, 'y': -1}, # ne
]

def is_xmas(x, y, data):
    # collect character pairs from corners in sets
    pair1 = (data[y + shifts[0]["y"]][x + shifts[0]["x"]], 
             data[y + shifts[1]["y"]][x + shifts[1]["x"]])
    pair2 = (data[y + shifts[2]["y"]][x + shifts[2]["x"]],
             data[y + shifts[3]["y"]][x + shifts[3]["x"]])
    # if both sets contain 'M' and 'S', return True
    if 'M' in pair1 and 'S' in pair1 and 'M' in pair2 and 'S' in pair2:
        return True
    return False

def main():
    data = []
    with open('data/04.data') as f:
        for row in f:
            data.append(row.strip())

    xmas_count = 0
    for y in range(len(data)):
        if not 0 < y < len(data) - 1:
            continue # can skip the first and last row
        for x in range(len(data[y])):
            if not 0 < x < len(data[y]) - 1:
                continue # can skip the first and last column
            if data[y][x] != 'A':
                continue
            if is_xmas(x, y, data):
                xmas_count += 1

    ic(xmas_count)

if __name__ == '__main__':
    main()
