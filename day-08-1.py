from icecream import ic
from collections import defaultdict

def main():
    antennas = defaultdict(list)
    max_x = False
    max_y = False
    with open('data/08.data') as f:
        for y, row in enumerate(f):
            for x, symbol in enumerate(row):
                if symbol in ['\n', '.']:
                    continue
                antennas[symbol].append((x, y))
        max_x = x - 1
        max_y = y

    antinodes = set()
    for symbol, coords in antennas.items():
        # go through all pairs of coords
        candidates = []
        for i, coord1 in enumerate(coords):
            for j, coord2 in enumerate(coords):
                if i == j:
                    continue
                x1, y1 = coord1
                x2, y2 = coord2
                x_diff = x1 - x2
                y_diff = y1 - y2
                antinode1 = (x1 + x_diff, y1 + y_diff)
                antinode2 = (x2 - x_diff, y2 - y_diff)
                candidates.append(antinode1)
                candidates.append(antinode2)
        for x, y in candidates:
            if x < 0 or y < 0 or x > max_x or y > max_y:
                continue
            antinodes.add((x, y))
    ic(len(antinodes))

    # 255 too high
    # draw the antinodes on a grid
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            char = '.'
            if (x, y) in antinodes:
                char = '#'
            for symbol, coords in antennas.items():
                if (x, y) in coords:
                    char = symbol
            print(char, end='')
        print()

if __name__ == '__main__':
    main()
