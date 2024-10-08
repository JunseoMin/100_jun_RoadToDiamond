import sys
input = sys.stdin.readline

N = int(input())
wli = []

dp = [1]*(N+1)

for i in range(N):
    wli.append(list(map(int,input().split())))

wli.sort()

for i in range(1,N+1):
    for j in range(1,i+1):
        if wli[i-1][1] > wli[j-1][1]:
            dp[i] = max(dp[i],dp[j] + 1)

ans = max(dp)
print(min(ans,N - ans))