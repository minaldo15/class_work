import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    inside = 0
    line = 0
    outside = 0
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        if x < x1 or x > x2 or y < y1 or y > y2:
            outside += 1
        elif x1 < x < x2 and y1 < y < y2:
            inside += 1
        else:
            line += 1
    print(f'#{t} {inside} {line} {outside}')
