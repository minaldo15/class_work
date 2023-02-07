T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    start = ans = 0
    end = N - 1
    while start <= end:
        mid = (end + start)//2
        if arr[mid] == D:
            ans = mid + 1
            break
        elif arr[mid] < D:
            start = mid + 1
        else:
            end = mid - 1
    print(f'#{t} {ans}')

