from icecream import ic
from functools import reduce

# Misunderstood instructions
# This searches all XMAS allowing the word to twist and turn
# instead of going in straight line

def find_matches_around(coord, data, char):
    x, y = coord
    shifts = [-1, 0, 1]
    matches = []
    for shift_y in shifts:
        for shift_x in shifts:
            if shift_x == 0 and shift_y == 0 and char == data[y][x]:
                assert False
            new_x = x + shift_x
            new_y = y + shift_y
            try:
                if data[new_y][new_x] == char:
                    matches.append((new_x, new_y))
            except IndexError:
                continue
    return matches

def get_xmas_count(x, y, data):
    # find all Ms around this X
    m_coords = find_matches_around((x, y), data, 'M')
    # find all As around all Ms
    a_coords = []
    for m_coord in m_coords:
        a_coords.extend(find_matches_around(m_coord, data, 'A'))
    ic(list(a_coords))
    # find all Ss around all As
    s_coords = []
    for a_coord in a_coords:
        s_coords.extend(find_matches_around(a_coord, data, 'S'))
    ic(list(s_coords))
    return len(s_coords)

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

    # ic(data)
    ic(xmas_count)

if __name__ == '__main__':
    main()
