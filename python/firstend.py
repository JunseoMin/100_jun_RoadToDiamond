import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    instr = input()
    print(instr[0]+instr[-2])