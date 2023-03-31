import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,A,B):
    global MIN
    if n == N:
        if len(A) == N//2:
            food_A = food_B = 0
            for i in range(N//2):
                for j in range(N // 2):
                    food_A += arr[A[i]][A[j]]
                    food_B += arr[B[i]][B[j]]
            MIN = min(MIN, abs(food_A-food_B))
        return
    dfs(n+1, A+[n], B)
    dfs(n+1, A, B+[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MIN = 20000*N*N
    dfs(0,[],[])
    print(f'#{tc} {MIN}')
