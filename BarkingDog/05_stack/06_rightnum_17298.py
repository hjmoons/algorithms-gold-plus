import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

answer = [-1] * N      # 결과 리스트
stack = [[A[0], 0]]
top = 0

for i in range(1, N):
    while stack:
        if stack[top][0] < A[i]:
            a, idx = stack.pop()
            answer[idx] = A[i]
            top -= 1
        else:
            break

    stack.append([A[i], i])
    top += 1

print(*answer)
