import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())

ans = combinations([i for i in range(n)],m)

for a in ans:
    for val in a:
        print(val , end=' ')
    print()