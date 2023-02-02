T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = int(input())
    c = [0] * 10 # 0부터 9까지 카드 개수 세기
    for i in range(N):
        c[num % 10] += 1
        num //= 10
    max = 0
    for k in range(0, 10):
        if c[k] >= max: # 크거나 같다고 해야 max에 큰 숫자(k) 할당 가능
            max = c[k]
            max_num = k
    print(f'#{t} {max_num} {max}')
