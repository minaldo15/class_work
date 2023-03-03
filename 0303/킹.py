arr = [[0]*8 for _ in range(8)]
col = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
dir = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}
king, rock, N = map(str, input().split())
ki, kj = 8-int(king[1]), col[king[0]]
ri, rj = 8-int(rock[1]), col[rock[0]]
print(ki, kj)
print(ri, rj)
for _ in range(int(N)):
    d = input()
    (di, dj) = dir[d]
    ni, nj = ki+di, kj+dj
    if (ni, nj) != (ri, rj):  # 킹이움직인 자리가 돌이 아니면
        if 0<=ni<8 and 0<=nj<8:
            ki,kj = ni,nj
    else:   # 킹이 돌을 밟으면
        if 0<=ni<8 and 0<=nj<8 and 0<=ri+di<8 and 0<=rj+dj<8:   # 킹과 돌 둘다 범위 안에 있으면
            ki,kj = ni,nj
            ri+=di
            rj+=dj
print(ki, kj)
print(ri, rj)
