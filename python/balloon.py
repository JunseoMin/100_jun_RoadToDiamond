import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
deq = deque(list(map(int,input().split())))

idx = 0

def cir_pop(n):
    if  n > 0:
        for _ in range(n):
            deq.append(deq.popleft())
    else:
        n *= -1
        for _ in range(n):
            deq.appendleft(deq.pop())
    return

while deq:
    n = deq.pop()
    cir_pop(idx + n)
    idx = idx + n
