from icecream import ic
from functools import reduce

coord_shifts = []
steps = 3
directions = [
    [1, 0], # east
    [0, 1], # south
    [-1, 0], # west
    [0, -1], # north
    [1, -1], # northeast
    [-1, -1], # northwest
    [1, 1], # southeast
    [-1, 1], # southwest
]
for direction in directions:
    direction_shifts = []
    for step in range(1, steps + 1):
        direction_shifts.append({
            'y': direction[0] * step, 
            'x': direction[1] * step
        })
    coord_shifts.append(direction_shifts)
ic(coord_shifts)

def get_xmas_count(x, y, data):
    xmas_count = 0
    # test all directions from X
    for shifts in coord_shifts:
        word = 'MAS'
        is_valid = True
        for shift, char in zip(shifts, word):
            new_x = x + shift["x"]
            new_y = y + shift["y"]
            if new_x < 0 or new_y < 0:
                is_valid = False
                break
            if new_y >= len(data) or new_x >= len(data[new_y]):
                is_valid = False
                break
            if data[new_y][new_x] != char:
                is_valid = False
                break
        if is_valid:
            xmas_count += 1
    return xmas_count


def main():
    data = []
    with open('data/04.data') as f:
        for row in f:
            data.append(row.strip())

    xmas_count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != 'X':
                continue
            xmas_count += get_xmas_count(x, y, data)

    ic(xmas_count)

if __name__ == '__main__':
    main()
