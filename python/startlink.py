import sys,math
input = sys.stdin.readline

N = int(input())
adds = []
for _ in range(N):
    adds.append(list(map(int,input().split())))

team1 = 0
team2 = 0
minimal = float('inf')

def dfs(team1, team2, minimal = float('inf'), depth=0, checked=[]):
    if depth == N:
        if abs(team1-team2) < minimal:
            minimal = abs(team1 - team2)
    
    for i in range(N):
        for j in range(N):
            if not ((i,j) in checked):
                team1 += (adds[i][j]+adds[j][i])
                checked.append((i,j))
                dfs(team1,team2,minimal,depth+1,checked)
                checked.pop()
                team1 -= adds[i][j]
            

dfs(team1,team2,minimal,0)

print(minimal)