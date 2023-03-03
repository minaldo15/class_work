import sys
sys.stdin = open('input.txt', 'r')

# def bfs(i, j):
#     q = [(i,j)]
#     v[i][j] = 1
#     cnt = 1
#     max = 0
#     while q:
#         ci, cj = q.pop(0)
#         for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
#             ni, nj = ci + di, cj + dj
#             if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
#                 q.append((ni, nj))
#                 v[ni][nj] = 1
#                 if arr[ci][cj] == arr[ni][nj]:
#                     cnt += 1
#                 else:
#                     if arr[ci][cj] == arr[ni+di][nj+dj]:
#                         if cnt + 1 > max:
#                             max = cnt + 1
#                     else:
#                         if cnt > max:
#                             max = cnt

N = int(input())
arr = [list(input()) for _ in range(N)]
# print(arr)
max = 0
for i in range(N):
    cnt = 1
    for j in range(1, N):
        if arr[i][j] == arr[i][j-1]:
            cnt += 1
        else:
            if N-1 > i >= 1 and (arr[i-1][j] == arr[i][j-1] or arr[i+1][j] == arr[i][j-1]):
                cnt += 1
            elif i == N-1 and arr[i-1][j] == arr[i][j-1]:
                cnt += 1
            elif i == 0 and arr[i + 1][j] == arr[i][j - 1]:
                cnt += 1
            else:
                if cnt > max:
                    max = cnt
                cnt = 1
    if cnt > max:  
        max = cnt  
# print(max)
arr1 = list(zip(*arr))
# print(arr1)
for i in range(N):
    cnt = 1
    for j in range(1, N):
        if arr1[i][j] == arr1[i][j-1]:
            cnt += 1
        else:
            if N-1 > i >= 1 and (arr1[i-1][j] == arr1[i][j-1] or arr1[i+1][j] == arr1[i][j-1]):
                cnt += 1
            elif i == N-1 and arr1[i-1][j] == arr1[i][j-1]:
                cnt += 1
            elif i == 0 and arr1[i + 1][j] == arr1[i][j - 1]:
                cnt += 1
            else:
                if cnt > max:
                    max = cnt
                cnt = 1
    if cnt > max:            
        max = cnt              
print(max)



