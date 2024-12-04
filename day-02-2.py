from icecream import ic

def is_level_safe(level):
    ascending = level[0] < level[1]
    for i in range(1, len(level)):
        difference = level[i - 1] - level[i]
        if not(1 <= abs(difference) <= 3):
            return False
        if ascending and difference > 0:
            return False
        elif not ascending and difference < 0:
            return False
    return True

def main():
    data = []
    with open('data/02.data') as f:
        for row in f:
            levels = row.split()
            data.append([int(x) for x in levels])

    safe_count = 0
    for level in data:
        is_safe = is_level_safe(level)
        if is_safe:
            safe_count += 1
            continue
        # try again by removing one index at a time
        to_try = range(len(level))
        for i in to_try:
            is_safe = is_level_safe(level[:i] + level[i + 1:])
            if is_safe:
                safe_count += 1
                break
    ic(safe_count)

if __name__ == '__main__':
    main()
