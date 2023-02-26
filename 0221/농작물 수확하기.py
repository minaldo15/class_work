import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cnt = 0
    i = 0
    for _ in range(N//2 + 1):
        lst = list(map(int, input()))
        cnt += sum(lst[N//2 - i:N//2+1 + i])
        i += 1

    i -= 1 # i가 한번 더 1추가되서 끝남, 한번빼주고 시작
    for _ in range(N//2 + 1, N):
        lst = list(map(int, input()))
        i -= 1
        cnt += sum(lst[N // 2 - i:N // 2 + 1 + i])

    print(f'#{t} {cnt}')
