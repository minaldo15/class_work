S = int(input())
lst = list(map(int, input().split()))
N = int(input())
for n in range(N):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(1, S + 1):
            if i % num == 0:
                if lst[i-1] == 0:
                    lst[i-1] = 1
                else:
                    lst[i-1] = 0
    else: # sex == 2
        pass
        if num > len(lst) // 2:
            K = len(lst) - num  # K는 num에서 양옆 최대 거리
        else:
            K = num - 1
        for i in range(K + 1):
            if lst[num-1-i] == lst[num-1+i]:
                if lst[num-1-i] == 0:
                    lst[num-1-i] = 1
                    lst[num-1+i] = 1
                else:
                    lst[num-1-i] = 0
                    lst[num-1+i] = 0
            else:
                break
if len(lst) > 20:
    for i in range(0, len(lst), 20):
        print(*lst[i:i + 20])
else: 
    print(*lst)
