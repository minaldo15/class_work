import sys
sys.stdin = open('input.txt', 'r')

# N -> 0, S -> 1
# d:1 -> lst.insert(0,lst.pop())
# d:-1 -> lst.append(lst.pop(0))
# 맞물리는 부분의 인덱스 -> (gear1[2],gear2[6]), (gear2[2],gear3[6]), (gear3[2], gear4[6])
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    gears = [[0]*8] + [list(map(int, input().split())) for _ in range(4)] + [[0]*8]
    moves = []
    score = 0
    for _ in range(K):
        n, d = map(int, input().split())
        moves.append((n, d))
    for move in moves:
        # 맞물려 있는 부분 확인(자성정보가 다른 부분)
        match = {1:[],2:[],3:[],4:[]}  # 1:(1-2), 2:(2-3), 3:(3-4)
        v = [0]*5
        for i in range(1, 4):
            if gears[i][2] != gears[i+1][6]:
                match[i].append(i+1)
                match[i+1].append(i)
        q = [move]
        while q:
            now = q.pop()
            if v[now[0]] == 0:
                if now[1] == 1:
                    gears[now[0]].insert(0, gears[now[0]].pop())
                else:
                    gears[now[0]].append(gears[now[0]].pop(0))
                v[now[0]] = 1
                for matchs in match[now[0]]:
                    if matchs:
                        q.append((matchs, now[1]*-1))

    if gears[1][0] == 1:
        score += 1
    if gears[2][0] == 1:
        score += 2
    if gears[3][0] == 1:
        score += 4
    if gears[4][0] == 1:
        score += 8
    print(f'#{tc} {score}')
