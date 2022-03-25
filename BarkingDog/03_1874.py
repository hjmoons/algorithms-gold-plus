import sys
from collections import deque

input = sys.stdin

seqs = deque()   # 입력 명령어 리스트

# Input
n = int(input.readline().strip())
for i in range(n):
    s = int(input.readline().strip())
    seqs.append(s)

stack = [0]  # 수열 담을 스택
top = 0     # 스택 top 위치
cur = 1     # 1 ~ n 표시 변수
result = []

while len(seqs) > 0:
    # 수열의 첫번째 수와 스택의 탑에 있는 수가 일치할 경우 pop 연산 수행
    if seqs[0] == stack[top]:
        stack.pop()
        seqs.popleft()
        result.append('-')
        top -= 1
        continue

    # 스택의 들어갈 수가 n이 될 때까지 스택에 push
    if cur < n + 1:
        stack.append(cur)
        result.append('+')
        top += 1
        cur += 1
    else:
        # 더 이상 스택에 들어갈 수가 없는 경우
        # 수열의 첫번째와 스택의 top에 있는 수가 다르면 더 이상 계산을 진행할 수 없음
        # 따라서 연산 중지
        if seqs[0] != stack[top]:
            top = -1
            break

if top == -1:
    print('NO')
else:
    for r in result:
        print(r)
