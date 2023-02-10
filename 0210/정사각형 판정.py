import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    lst_x = []
    lst_y = []
    ans = 1
    for y in range(N):
        for x in range(N):
            if arr[y][x] == '#':
                lst_y.append(y)
                lst_x.append(x)
    min_x, max_x = min(lst_x), max(lst_x)
    min_y, max_y = min(lst_y), max(lst_y)
    if max_x - min_x == max_y - min_y:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if arr[y][x] != '#':
                    ans = 0
    else:
        ans = 0
    if ans == 1:
        print(f'#{t} yes')
    else:
        print(f'#{t} no')




