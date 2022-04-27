import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

lcs = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            lcs[i][j] += 1

for d in lcs:
    print(d)
print()

dp = [0] * len(lcs[0])
for i in range(len(str1)):
    count = 0
    print(dp)
    print(lcs[i])
    print()

    for j in range(len(str2)):
        if j == 0 and lcs[i][j] == 1:
            dp[j] = 1
            count = 1
        else:
            if dp[j-1] > count:
                count = dp[j-1]

            if lcs[i][j] == 1:
                dp[j] = count + 1

print(dp)
print(max(dp))