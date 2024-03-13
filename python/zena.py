for i in range(2,9,2):
    print(("{:^5}".format("*"*i))*2)
    if i == 2:
        break

for i in range(9,0,-2):
    print("{:^10}".format("*"*i))