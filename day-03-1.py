from icecream import ic
from regex import findall

def main():
    data = ""
    with open('data/03.data') as f:
        data = f.read()

    matches = findall(r'(mul\()(\d{1,3},\d{1,3})\)', data)

    sumproduct = 0
    for match in matches:
        _, values = match
        # apply parseint to values
        a, b = map(int, values.split(','))
        sumproduct += a * b
    ic(sumproduct)

if __name__ == '__main__':
    main()
