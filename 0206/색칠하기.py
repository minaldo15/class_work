import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    red = []
    blue = []
    result = 0
    for n in range(N):
        a, b, A, B, color = map(int, input().split())
        if color == 1:
            for i in range(a, A + 1):
                for j in range(b, B + 1):
                    if [i,j] not in red:
                        red.insert(-1, [i,j])
        else:
            for i in range(a, A + 1):
                for j in range(b, B + 1):
                    if [i,j] not in blue:
                        blue.insert(-1, [i,j])

    for dot in red:
        if dot in blue:
            result += 1
    print(f'#{t} {result}')


