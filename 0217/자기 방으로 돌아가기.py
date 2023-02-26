import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    room = [0]*201
    N = int(input())
    for n in range(N):
        a, b = map(int, input().split()) # (1, 5) 과 (6, 8)일 경우 3과 4의 동선이 겹침
        a, b = (a + 1)//2, (b + 1)//2 # 5와 6을 같은 숫자인 3으로 만들어줌으로써 겹친것으로 체크되게 하기
        for i in range(min(a,b), max(a, b)+1):
            room[i] += 1

    print(f'#{t} {max(room)}')
