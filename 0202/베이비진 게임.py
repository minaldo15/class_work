T = int(input())
for t in range(1, T + 1):
    num = int(input())
    flag = 0
    run = 0
    tri = 0
    c = [0] * 10
    for i in range(6):
        c[num  % 10] += 1
        num //= 10
    i = 0
    while i < 10: 
        if c[i] >=  3: # tri 검증
            tri += 1
            c[i] -= 3
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 검증
            run += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            continue
        i += 1
    if tri + run == 2:
        flag = 1
    print(f'#{t} {flag}')


    

