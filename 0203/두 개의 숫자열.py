f = open('input.txt')
input = f.readline
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # K = abs(N - M) + 1 # 마주보는 위치의 개수
    ans = 0
    if N < M:
        for k in range(M - N + 1):
            cnt = 0
            for i in range(N):
                m = A[i] * B[i + k]
                cnt += m
            if ans < cnt:
                ans = cnt
    else:
        for k in range(N - M + 1):
            cnt = 0
            for i in range(M):
                m = A[i + k] * B[i]
                cnt += m
            if ans < cnt:
                ans = cnt
    print(f'#{t} {ans}')


    
