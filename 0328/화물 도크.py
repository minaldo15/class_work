import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    table = [arr[0]]
    j = 0
    for i in range(1, len(arr)):
        if arr[i][0]>=arr[j][1]:
            table.append(arr[i])
            j = i
    print(f'#{tc} {len(table)}')
