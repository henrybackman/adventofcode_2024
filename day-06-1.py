from icecream import ic

def print_lab(lab_map, guard):
    for y, row in enumerate(lab_map):
        for x, cell in enumerate(row):
            if (x, y) == guard.get_location():
                print(guard.direction, end='')
            else:
                if (x, y) in guard.visited:
                    print('o', end='')
                    continue
                print(cell, end='')
        print()
    print()

class Guard():
    def __init__(self, lab, x, y, direction):
        self.lab = lab
        self.x = x
        self.y = y
        self.direction = direction
        self.visited = set()
        self.visited.add((x, y))
        self.tail = set()
        self.tail.add((x, y, direction))
        self.is_out = False
        self.is_loop = False

    def step(self, lab_map):
        # find next place to step
        new_x = 0
        new_y = 0
        while True:
            # get cell in front of guard
            if self.direction == 'U':
                new_y = self.y - 1
                new_x = self.x
            elif self.direction == 'D':
                new_y = self.y + 1
                new_x = self.x
            elif self.direction == 'L':
                new_x = self.x - 1
                new_y = self.y
            elif self.direction == 'R':
                new_x = self.x + 1
                new_y = self.y
            # stepping out of the lab
            if not (0 <= new_y < len(lab_map)) or not (0 <= new_x < len(lab_map[0])):
                self.is_out = True
                print('out of lab')
                break
            # entering a loop
            if (new_x, new_y, self.direction) in self.tail:
                self.is_loop = True
                print('loop')
                break
            contents = lab_map[new_y][new_x]
            if contents == '#':
                # obstacle, rotate
                self.rotate()
                continue
            self.x = new_x
            self.y = new_y
            self.visited.add((new_x, new_y))
            self.tail.add((new_x, new_y, self.direction))
            # print_lab(lab_map, self)
            break

    def get_location(self):
        return self.x, self.y

    # rotate 90 degrees to right
    def rotate(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'
    

class Lab():
    def __init__(self, lab_map, guard):
        self.lab_map = lab_map
        self.guard = guard

    def step(self):
        self.guard.step(self.lab_map)


def main():
    lab_map = []
    guard_x = 0
    guard_y = 0
    with open('data/06.data') as f:
        for y, row in enumerate(f):
            details = []
            for x, char in enumerate(row):
                if char == '\n':
                    continue
                if char == '^':
                    guard_x = x
                    guard_y = y
                    details.append('.')
                    continue
                details.append(char)
            lab_map.append(details)

    # 41 is correct
    guard = Guard(lab_map, guard_x, guard_y, 'U')
    lab = Lab(lab_map, guard)
    while True:
        lab.step()
        # ic(len(guard.visited), len(guard.tail))
        if guard.is_out or guard.is_loop:
            break
    ic(len(guard.visited))
    # print_lab(lab, guard)
    # 5338, 5337 too high
    # 5330 too low
    # 5331 is correct, off by one
    # 5332 is too high

if __name__ == '__main__':
    main()
