from icecream import ic
from collections import Counter
def main():
    xs = []
    ys = []
    with open('data/01.data') as f:
        for row in f:
            x , y = [int(a) for a in row.split()]
            xs.append(x)
            ys.append(y)

    counter = Counter(ys)

    similarity_score = 0
    for x in xs:
        similarity_score += x * counter[x]
    
    ic(similarity_score)

if __name__ == '__main__':
    main()
