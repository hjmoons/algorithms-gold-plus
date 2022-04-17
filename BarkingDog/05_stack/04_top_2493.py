import sys

input = sys.stdin.readline

n = int(input().rstrip())
tops = list(map(int, input().rstrip().split()))
stack = []      # 높이 스택
i_stack = []    # 인덱스 스택
st = -1         # 스택의 탑
answer = []     # 결과값 리스트

for i in range(n):
    if i == 0:
        stack.append(tops[i])
        i_stack.append(i)
        answer.append(i)
        st += 1
        continue

    while st > -1:
        if stack[st] > tops[i]:
            break

        stack.pop()
        i_stack.pop()
        st -= 1

    if st > -1:
        answer.append(i_stack[st])
    else:
        answer.append(0)

    stack.append(tops[i])
    i_stack.append(i + 1)
    st += 1

for a in answer:
    print("{0} ".format(a), end='')