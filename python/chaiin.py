n = int(input())
ans = 0
for _ in range(n):
    instr = input()
    alpha = []
    flag = True
    
    for i in range(len(instr)-1):
        if flag:
            if instr[i] == instr[i+1]:
                if not instr[i] in alpha:
                    alpha.append(instr[i])
            elif instr[i+1] in alpha:
                flag = False
                break
    print(alpha)
            
    if flag:    #입력이 그룹단어라면
        ans+=1
    else: #그룹단어가 아니라면
        pass

print(ans)