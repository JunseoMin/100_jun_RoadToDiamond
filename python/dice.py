n1,n2,n3 = 3,2,6
nlist = [n1,n2,n3]
tmp = 0
s_num = 0

for i in range(len(nlist)):
    if nlist[i] in nlist[:i] + nlist[i+1:]:
        snum = nlist[i]
        tmp += 1
tmp /= 2
        
if tmp == 0:
    print(max(nlist) * 100)
elif tmp == 1:
    print(1000 + snum*100)
else:
    print(10000 + n1 * 1000)
