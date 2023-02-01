import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = input().split()
    t_lst = list(map(int, input().split()))
    K = int(N) - int(M) + 1
    k_lst = []
    for k in range(K):
        k_lst.append(sum(t_lst[k:k+int(M)]))
    print(f'#{t} {max(k_lst) - min(k_lst)}')






