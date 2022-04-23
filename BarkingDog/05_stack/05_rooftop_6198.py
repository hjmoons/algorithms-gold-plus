import sys

input = sys.stdin.readline

N = int(input().rstrip())
stack = []      # 옥상 스택
answer = 0      # 결과값

# 첫번째 옥상의 높이는 바로 스택에 추가
h = int(input().rstrip())
stack.append(h)
top = 0

for _ in range(N - 1):
    h = int(input().rstrip())

    while top > -1:
        if stack[top] > h:
            answer += top + 1
            break

        stack.pop()
        top -= 1

    stack.append(h)
    top += 1

print(answer)
