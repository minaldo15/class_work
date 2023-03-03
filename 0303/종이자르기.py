R, C = map(int, input().split())
row = [0,R]
col = [0,C]
N = int(input())
for _ in range(N):
    # 가로: 0 세로: 1
    rc, k = map(int, input().split())
    if rc == 1:
        row.append(k)
    else:
        col.append(k)
row.sort()
col.sort()
max_r = 0
max_c = 0
for i in range(1, len(row)):
    r = row[i] - row[i-1]
    if r > max_r:
        max_r = r
for i in range(1, len(col)):
    c = col[i] - col[i-1]
    if c > max_c:
        max_c = c
ans = max_r*max_c
print(ans)



