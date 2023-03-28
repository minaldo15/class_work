import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    v = [0]*12
    ans = run = tri = 0
    for num in lst:
        v[num] += 1
    i = 0
    while i < 10:
        if v[i] >= 3:
            tri += 1
            v[i] -= 3
            i -= 1
        if 1 <= v[i] < 3 and 1 <= v[i+1] < 3 and 1 <= v[i+2] < 3:
            run += 1
            v[i] -= 1
            v[i+1] -= 1
            v[i+2] -= 1
            i -= 1
        i += 1
    if run + tri == 2:
        ans = 1
    print(f'#{tc} {ans}')
