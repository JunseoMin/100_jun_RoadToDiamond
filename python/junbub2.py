n,b = map(int,input().split())
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ans = ''

while(n>=b):
    left = n%b
    tmp = ''
    n = n//b
    # print(n//b)
    if left<10:
        tmp = str(left)
        tmp += ans
        ans = tmp
    else:
        tmp = alpha[left-10]
        tmp += ans
        ans = tmp


left = n%b
tmp = ''
if left<10:
    tmp = str(left)
    tmp += ans
    ans = tmp
else:
    tmp = alpha[left-10]
    tmp += ans
    ans = tmp

print(ans)