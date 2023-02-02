f = open('input.txt')
input = f.readline

for t in range(1, 11):
    cnt = int(input())
    lst = list(map(int, input().split()))
    for n in range(cnt):
        maxi = lst[0]
        max_i = 0
        mini = lst[0]
        min_i = 0
        for i in range(1, 100):
            if lst[i] >= maxi:
                maxi = lst[i]
                max_i = i
            if lst[i] <= mini:
                mini = lst[i]
                min_i = i
        lst[max_i] -= 1
        lst[min_i] += 1
    print(f'#{t} {max(lst) - min(lst)}')