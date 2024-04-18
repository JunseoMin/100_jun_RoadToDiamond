import sys,math
input = sys.stdin.readline
n = int(input());
nli = [];sum = 0

for _ in range(n):
    _in = int(input())
    nli.append(_in)
    sum+= _in
    
print(math.floor((sum - (max(nli) + min(nli)))/(n-2)))