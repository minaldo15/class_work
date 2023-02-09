import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
T = int(input())
for t in range(1, T + 1):
    A, B = input().split()
    N = len(A) # i
    M = len(B) # j
    cnt = 0
    i = j = 0
    while i < N:
        if A[i] != B[j]:
            i += 1
            j = 0
        else: # A[i] == B[j]:
            i += 1
            j += 1
            if j == M - 1:
                if A[i] == B[j]:
                    cnt += 1
                    i += 1
                    j = 0

    ans = N - (M-1)*cnt
    print(f'#{t} {ans}')