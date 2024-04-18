import sys
a = []
tmp = 0
for _ in range(3):
    a.append(int(input()))
    
if sum(a) != 180:
    print("error")
    sys.exit()
    
for i in range(3):
    tmp = a.count(a[i])
    if  tmp == 2:
        print("Isosceles")
        sys.exit()
    if tmp == 3:
        print("Equilateral")
        sys.exit()
        
print("Scalene")