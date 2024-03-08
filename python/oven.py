# h,m = map(int,input().split())
h = 23
m = 48

# time = input()
time = 25

added = (m + time) // 60
print(str((h + added) % 24) + ' ' + str((m + time) % 60))