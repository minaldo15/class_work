import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    if flag == 1:
        # 행 검증
        for lst_1 in arr:
            count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for num in lst_1:
                if num in count:
                    count.remove(num)
            if len(count) > 0:
                flag = 0
                break
            else:
                flag = 1
    if flag == 1:
        # 열 검증(전치행렬)
        arr_1 = list(zip(*arr))
        for lst_2 in arr_1:
            count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for num in lst_2:
                if num in count:
                    count.remove(num)
            if len(count) > 0:
                flag = 0
                break
            else:
                flag = 1
    if flag == 1:
        # 박스 검증
        for k in range(3):
            for l in range(3):
                lst_3 = []
                count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(3):
                    for j in range(3):
                        lst_3.append(arr[i+k*3][j+l*3])

                if set(lst_3) != set(count):
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 0:
                break

    print(f'#{t} {flag}')
