import sys
sys.stdin = open('input.txt', 'r')

A =[x for x in range(1, 13)]

def dfs(i, cnt, sm):
    global ans
    #  종료조건(i 에 관련)=> 정답처리는 이곳에서
    if cnt > N:
        return
    if sm > K:
        return
    if i == 12:
        if cnt == N and sm == K:
            ans += 1
        return
    # 하부 호출
    p.append(A[i])
    dfs(i+1, cnt+1, sm+A[i])    # 사용하는 경우
    p.pop()
    dfs(i + 1, cnt, sm)         # 사용하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    p = []
    ans = 0
    #   i, cnt, sm
    dfs(0,0,0)
    print(f'#{tc} {ans}')
