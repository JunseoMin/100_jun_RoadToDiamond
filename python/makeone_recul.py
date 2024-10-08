import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())

memo = {}

def dp(n):
    if n == 1:
        return 0

    if n < 1:
        return float('inf')

    if n in memo:
        return memo[n]
    
    memo[n] = 1 + min(dp(n-1),dp(n//3) if not n%3 else float('inf'),dp(n//2) if not n%2 else float('inf'))
    return memo[n]

print(dp(n))