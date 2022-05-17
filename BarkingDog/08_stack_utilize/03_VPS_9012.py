import sys

input = sys.stdin.readline

n = int(input().rstrip())
result = []
for i in range(n):
    vps = input().rstrip()

    stack = []
    top = -1
    check = True
    for v in vps:
        # 스택에 값이 없는 경우
        if top < 0:
            # ')'가 시작이면 VPS가 아닌 경우
            if v == ')':
                check = False
                break
            stack.append(v)
            top += 1
            continue

        # 스택의 탑과 비교하려는 대상이 '(', ')' 경우
        # VPS 일치하므로 팝 연산 수행
        # 일치하지 않을경우 스택에 푸쉬
        if v == ')' and stack[top] == '(':
            stack.pop()
            top -= 1
        else:
            stack.append(v)
            top += 1

    # 스택에 괄호가 남으면 VPS가 아닌 경우
    if top > -1:
        check = False

    if check:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)