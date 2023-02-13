import sys
sys.stdin = open('input.txt', 'r')

# def pascal(N):
#     lst = []
#     if N == 1:
#         return [1]
#     elif N == 2:
#         return [1,1]
#     else:
#         lst.append(1)
#         for i in range(len(pascal(N-1)) - 1):
#             lst.append(pascal(N - 1)[i] + pascal(N - 1)[i+1])
#         lst.append(1)
#         return lst

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        arr[i][0] = 1
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{t}')
    for lst in arr:
        lst_0 = ' '.join(map(str, lst))
        print(lst_0.rstrip('0 '))





