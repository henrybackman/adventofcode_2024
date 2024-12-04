def main():
    xs = []
    ys = []
    with open('data/01.data') as f:
        for row in f:
            x , y = [int(a) for a in row.split()]
            xs.append(x)
            ys.append(y)

    xs.sort()
    ys.sort()

    sum = 0
    for x, y in zip(xs, ys):
        sum += abs(x - y)
    
    print(f"sum of differences: {sum}")

if __name__ == '__main__':
    main()
