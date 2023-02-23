import sys
sys.stdin = open('input.txt', 'r')

def operator(op, a, b):
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

for t in range(1, 2):
    N = int(input())
    L = [0] * (N - 1)
    R = [0] * (N - 1)
    heap = [0] * (N + 1)
    for _ in range(N):
        lst = list(input().split())
        if len(lst) > 2:
            p, op, l, r = int(lst[0]), lst[1], int(lst[2]), int(lst[3])
            heap[p] = op
            L[p] = l
            R[p] = r
        else:
            c, num = int(lst[0]), int(lst[1])
            heap[c] = num

    for i in range(N - 2, 0, -1):
        if L[i]:
            heap[i] = operator(heap[i], heap[L[i]], heap[R[i]])
    ans = heap[1]
    print(f'#{t} {int(ans)}')
