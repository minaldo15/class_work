import sys
sys.stdin = open('input.txt', 'r')

def enq(n):
    global last
    last += 1       # 완전이진트리에 마지막 정점을 추가하고
    heap[last] = n  # 마지막 정점에 저장
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]: # 부모가 있고, 부모 < 자식 조건 검사를 위해
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 옮긴 자리에서 부모와 비교하기 위해
        p = c//2
    return

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0]*(N+1)
    last = 0
    sum = 0
    for i in lst:
        enq(i)

    while N > 1:
        N = N//2
        sum += heap[N]
    print(f'#{t} {sum}')
