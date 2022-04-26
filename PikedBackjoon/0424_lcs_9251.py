import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0 for _ in range(len(str1))] for _ in range(len(str2))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] += 1

for d in dp:
    print(d)

for i in range(1, len(str1)):
    count = 0
    print(dp[0], i)
    for j in range(len(str2)):
        if j == 0 and dp[i][j] == 1:
            dp[0][j] = 1
        #elif dp[0][j] >= 1:
            #if dp[i][j] == 1:
            #count = dp[i][j]

        count = dp[i][j]

print(dp[0])