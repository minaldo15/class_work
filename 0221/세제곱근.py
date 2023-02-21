T = int(input())
for t in range(1, T + 1):
    N = int(input())
    x = round(N**(1/3),5)
    y = round(N ** (1 / 3),1)
    if x == y:
        print(f'{y:.0f}')
    else:
        print(-1)


