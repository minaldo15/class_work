import sys
sys.stdin = open('input.txt', 'r')

def f(i, k):
    global min
    global fcnt
    fcnt += 1
    if i == k:
        s = 0
        for y in range(N): # 재귀로 구해진 p(arr의 각 행에서 인덱스 j의 순열)을 활용한 최솟값 구하기
            s += arr[y][p[y]]
        if s < min:
            min = s

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i] # 순열을 이용한 각 경우의 수를 구하기
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    p = [n for n in range(N)] # 각행의 인덱스 배열(0,1,2...)
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for y in range(N): # arr(0,0) 부터 (N,N)을 더한 임의의 최솟값 설정
        sum += arr[y][y]
    min = sum
    fcnt = 0
    f(0, N)
    print(f'#{t} {min}')
    print(fcnt)
