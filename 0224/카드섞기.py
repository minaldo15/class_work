import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
print(S)
new = [0]*(N)
for i in range(N):
    j = S[i]
    print(j)
    new[j] = j
S = new
print(S)
for i in range(N):
    j = S[i]
    print(j)
    new[j] = j
print(S)