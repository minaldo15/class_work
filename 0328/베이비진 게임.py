import sys
sys.stdin = open('input.txt', 'r')

def check1():
    global ans
    Run = tri = 0
    i = 0
    while i < 10:
        if v1[i] >= 3:
            tri += 1
            v1[i] -= 3
            i -= 1
        if 1 <= v1[i] < 3 and 1 <= v1[i+1] < 3 and 1 <= v1[i+2] < 3:
            Run += 1
            v1[i] -= 1
            v1[i+1] -= 1
            v1[i+2] -= 1
            i -= 1
        i += 1
    if Run + tri >= 1:
        ans = 1

def check2():
    global ans
    Run = tri = 0
    i = 0
    while i < 10:
        if v2[i] >= 3:
            tri += 1
            v2[i] -= 3
            i -= 1
        if 1 <= v2[i] < 3 and 1 <= v2[i+1] < 3 and 1 <= v2[i+2] < 3:
            Run += 1
            v2[i] -= 1
            v2[i+1] -= 1
            v2[i+2] -= 1
            i -= 1
        i += 1
    if Run + tri >= 1:
        ans = 2

T = int(input())
for tc in range(1, T+1):
    p1 = []
    p2 = []
    lst = list(map(int, input().split()))
    for i in range(6):
        p1.append(lst[i*2])
        p2.append(lst[i*2-1])
    ans = 0
    for i in range(3, 7):
        v1 = [0] * 12
        v2 = [0] * 12
        if ans == 0:
            for j in range(i):
                v1[p1[j]] += 1
                check1()
                if ans == 0:
                    v2[p2[j]] += 1
                    check2()
                else:
                    break
    print(f'#{tc} {ans}')
