import sys

input = sys.stdin.readline

N = int(input())

inst = list(map(int,input().split()))

def stacksum(idx_start):
    if 