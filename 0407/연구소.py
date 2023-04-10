import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
from copy import deepcopy
from collections import deque

N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
wall = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i,j))
        if arr[i][j] == 1:
            wall += 1
        if arr[i][j] == 2:
            virus.append((i,j))

all_case = list(combinations(empty, 3))
answer = N*M

for case in all_case:
    new_virus = 0
    flag = 0
    status = deepcopy(arr)
    for i,j in case:
        status[i][j] = 1

    now_virus = deque(virus)

    while now_virus:
        ci, cj = now_virus.popleft()
        for di, dj in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and status[ni][nj] == 0:
                status[ni][nj] = 2
                new_virus += 1
                if answer <= new_virus:
                    flag = 1
                    break
                now_virus.append((ni,nj))
        if flag:
            break
    answer = min(answer, new_virus)

print(N*M - len(virus) - wall - answer - 3)




