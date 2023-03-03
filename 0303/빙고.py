import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int, input().split())) for _ in range(5)]
check = []
for _ in range(5):
    for num in list(map(int, input().split())):
        check.append(num)
for k in range(11):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == check[k]:
                arr[i][j] = 0
for k in range(11, 25):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == check[k]:
                arr[i][j] = 0
    for lst in arr:
        if lst == [0,0,0,0,0]:
            cnt += 1
    for lst in list(zip(*arr)):
        if lst == (0,0,0,0,0):
            cnt += 1
    if [arr[a][a] for a in range(5)] == [0,0,0,0,0]:
        cnt += 1
    if [arr[b][4-b] for b in range(5)] == [0, 0, 0, 0, 0]:
        cnt += 1
    if cnt >= 3:
        ans = k + 1
        break

print(ans)








