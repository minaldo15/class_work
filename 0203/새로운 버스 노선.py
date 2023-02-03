T = int(input())
for t in range(1, T + 1):
    N = int(input())
    station = []
    for n in range(N):
        bus = []
        type, A, B = map(int, input().split())
        if type == 1:
            for i in range(A, B + 1):
                bus.append(i)
        if type == 2:
            bus.append(A)
            bus.append(B)
            for i in range(A, B + 1):
                if i != A and i != B:
                    if A % 2 == 0:
                        if i % 2 == 0:
                            bus.append(i)
                    else:
                        if i % 2 == 1:
                            bus.append(i)
        if type == 3:
            bus.append(A)
            bus.append(B)
            for i in range(A, B + 1):
                if i != A and i != B:
                    if A % 2 == 0:
                        if i % 4 == 0:
                            bus.append(i)
                    else:
                        if i % 3 == 0 and i % 10 != 0:
                            bus.append(i)
        for num in bus:
            station.append(num)

    count = [0] * max(station)
    for num in station:
        count[num - 1] += 1
# 중복된 정류장 개수세기
    print(f'#{t} {max(count)}')

