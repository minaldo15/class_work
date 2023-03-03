N = int(input())
arr = list(map(int, input().split()))
max = 1
cnt = 1
# 오름차순
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        cnt += 1
        if cnt>max:
            max = cnt
    else:
        cnt = 1
cnt = 1
# 내림차순
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        cnt += 1
        if cnt>max:
            max = cnt
    else:
        cnt = 1
print(max)
        

