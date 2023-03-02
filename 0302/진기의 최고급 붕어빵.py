import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    cus = list(map(int, input().split()))
    cus.sort()
    for i in range(len(cus)):
        if cus[i] >= M and i+1 <= K*(cus[i]//M):
            ans = 'Possible'
        else:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')
