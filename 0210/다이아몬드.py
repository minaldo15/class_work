T = int(input())
for t in range(1, T + 1):
    a = input()
    k = len(a)
    print('..#..'+'.#..'*(k-1))
    print('.#.#.'+'#.#.'*(k-1))
    print(a.replace('', '.#.')[1:-1])
    print('.#.#.' + '#.#.' * (k - 1))
    print('..#..' + '.#..' * (k - 1))