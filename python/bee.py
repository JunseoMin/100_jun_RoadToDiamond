n = int(input())
num = 0
level = 0

while True:
    num_curr = num + 6*level
    if num < n-1 < num_curr:
        print(level+1)
        break
    num = num_curr
    level += 1
    