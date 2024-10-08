import sys

input = sys.stdin.readline

sub_s1 = []
sub_s2 = []

instr1 = input().strip()
instr2 = input().strip()
N = len(instr1)
M = len(instr2)

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if instr1[i] == instr2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[N-1][M-1])