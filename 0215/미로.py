import sys
sys.stdin = open('input.txt', 'r')

def dfs(si, sj):
    stk = [(si, sj)]  # 필요한 자료형, 플래그, 변수 등 선언
    v[si][sj] = 1  # 초기 위치 처리
    ci, cj = si, sj  # 기준점 저장

    while True:
        # 4/8/연결된 링크... 범위 내/미방문/'1'아니면 탐색
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj  # 다음 좌표 계산
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != '1':
                ci, cj = ni, nj
                stk.append((ci, cj))
                v[ci][cj] = 1
                break
        else:
            if stk:
                ci, cj = stk.pop()
            else:
                break

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    # 시작/종료 좌표 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    dfs(si, sj)
    ans = v[ei][ej]
    print(f'#{tc} {ans}')









