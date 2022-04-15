import sys

input = sys.stdin.readline

k = int(input().rstrip())
money = []

for _ in range(k):
    n = int(input().rstrip())
    if n == 0:
        money.pop()
    else:
        money.append(n)

sum = 0
for m in money:
    sum += m

print(sum)