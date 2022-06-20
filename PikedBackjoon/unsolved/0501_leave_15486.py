# 다시 풀어볼 문제

import sys

input = sys.stdin.readline

N = int(input().rstrip())

money = [0] * (N + 1)

cons = []
for _ in range(N):
    T, P = map(int, input().rstrip().split())
    cons.append([T, P])

for i in reversed(range(N)):
    T, P = cons[i]
    if i + T > N:
        continue

    next = i + T
    if next < N:
        max_money = 0
        for j in range(i + T, N):
            if max_money < money[j] + P:
                max_money = money[j] + P
                next = j

    money[i] = money[next] + P

print(max(money))