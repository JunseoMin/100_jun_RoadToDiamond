import sys
input = sys.stdin.readline

while True:
    inst = input()
    inst = inst[:-1]

    if inst == '.':
        break

    gwal = {'[':0,
            '{':0,
            '(':0}

    flag = True

    for s in inst[:-1]:
        if s == '(':
            tmp = gwal['(']
            tmp += 1
            gwal['('] = tmp
        elif s == '{':
            tmp = gwal['{']
            tmp += 1
            gwal['{'] = tmp
        elif s == '[':
            tmp = gwal['[']
            tmp += 1
            gwal['['] = tmp
            
        elif s == ')':
            tmp = gwal['(']
            tmp -= 1
            gwal['('] = tmp
            if tmp < 0:
                flag = False
                break
        elif s == '}':
            tmp = gwal['{']
            tmp -= 1
            gwal['{'] = tmp
            if tmp < 0:
                flag = False
                break
        elif s == ']':
            tmp = gwal['[']
            tmp -= 1
            gwal['['] = tmp
            if tmp < 0:
                flag = False
                break
    for _,v in gwal.items():
        if v:
            flag = False

    if flag:
        print("yes")
    else:
        print("no")

