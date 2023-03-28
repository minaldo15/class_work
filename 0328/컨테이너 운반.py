import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nlst = list(map(int, input().split()))
    mlst = list(map(int, input().split()))
    nlst.sort()
    mlst.sort()
    ans = 0
    w = nlst.pop()  # 화물 무게
    t = mlst.pop()  # 트럭 적재용량
    while nlst and mlst:
        if w <= t:
            ans += w
            w = nlst.pop()
            t = mlst.pop()
        else:
            w = nlst.pop()
    if w <= t:
        ans += w

    print(f'#{tc} {ans}')
