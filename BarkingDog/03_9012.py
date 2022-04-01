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
        #print(stack)
        if top < 0:
            if v == ')':
                check = False
                break
            stack.append(v)
            top += 1
            continue

        if v == ')' and stack[top] == '(':
            stack.pop()
            top -= 1
        else:
            stack.append(v)
            top += 1

    if top > -1:
        check = False

    if check:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)