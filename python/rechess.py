import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

chess = []
li1 = []
li2 = []

# [] * M for _ in range(N)

for i in range(N):
    tmp = []
    instr = input().strip()
    for alpha in instr:
        if alpha == "B":
            tmp.append(0)
        else:
            tmp.append(1)
    chess.append(tmp)


for i in range(N - K):
    tmp1 = 0
    tmp2 = 0
    for j in range(M - K):
        for a in range(K):
            for b in range(K):
                if chess[i][j] != li1[a][b]:
                    tmp1 += 1
                if chess[i][j] != li2[a][b]:
                    tmp2 += 1
            

        pass

'''
4 4 3
BBBB
BBBB
BBBW
BBWB
'''