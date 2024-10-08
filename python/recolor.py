import sys

input= sys.stdin.readline

N,M,K = map(int,input().split())

chess = []

for _ in range(N):
  for __ in range(M):
    chess.append(list(map(int,input().split())))

print(chess)