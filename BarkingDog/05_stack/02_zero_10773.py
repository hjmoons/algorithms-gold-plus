import sys

input = sys.stdin.readline

k = int(input().rstrip())
money = []

for _ in range(k):
    n = int(input().rstrip())
    if n == 0:              # 0 일경우 돈 리스트에서 팝
        money.pop()
    else:                   # 그 외에는 다 푸쉬
        money.append(n)

# 리스트의 있는 수의 총합
sum = 0
for m in money:
    sum += m

print(sum)