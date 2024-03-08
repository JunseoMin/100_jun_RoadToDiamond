total = int(input())
n = int(input())

real = 0

for _ in range(n):
    price , numbers = map(int,input().split())
    real += price * numbers

print(real)

if real != total:
    print('No')
else:
    print('Yes')