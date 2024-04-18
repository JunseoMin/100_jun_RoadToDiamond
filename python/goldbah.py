import sys
input = sys.stdin.readline

check = [1 for i in range(1000001)]
sosus = []

check[0] = 0
check[1] = 0

for i in range(2,1000001):
    if not check[i]:
        continue

    sosus.append(i)
    
    for j in range(i*2,1000001,i):
        check[j] = 0

N = int(input())

for _ in range(N):
    n = int(input())
    cnt = 0
    
    for i in sosus:
        j = n-i
        if check[i] and check[j] and i>=j:
            cnt += 1

    print(cnt)