import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
slist = deque(list(map(int,input().split())))
stack = deque()

for target in range(1,N+1):
    while slist:    
        first = slist.popleft()
        if first == target:
            continue
        else:
            stack.append(first)

        