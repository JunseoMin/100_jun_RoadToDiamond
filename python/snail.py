import sys

a,b,v = map(int,sys.stdin.readline().split())
curr = 0
day = 0
day_per = a-b

while curr < v:
    curr += day_per
    day += 1

if curr + b >= v:
    print(day-1)
else:
    print(day)