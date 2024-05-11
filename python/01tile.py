# import sys
# sys.setrecursionlimit(100000000)
# N = int(input())

# checked = {}
# i = 0
# zero = "00"
# one = '1'

# def dp(left, cnt = 0, nums = ""):
#     if left < 0:
#         return 0
    
#     if  not left:
#         return 1

#     if nums in checked:
#         return checked[nums]
    
#     else:
#         checked[nums] = dp(left - 1, cnt, nums + one) + dp(left - 2, cnt, nums + zero)
#         return checked[nums]

# dp(N)
# print(checked['']%15746)
import sys
N = int(input())

if N == 1:
    print(1)
    sys.exit()

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])
