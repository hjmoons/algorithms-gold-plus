import sys

input = sys.stdin.readline

n = int(input().rstrip())
result = []
for _ in range(n):
    loger = list(input().rstrip())  # 입력된 문자열

    str_1 = []  # 커서 왼쪽 문자열
    str_2 = []  # 커서 오른쪽 문자열

    for l in loger:
        if l == '<':
            if len(str_1) != 0:    # 커서가 왼쪽으로 이동한 경우
                str_2.append(str_1.pop())
        elif l == '>':
            if len(str_2) != 0:  # 커서가 오른쪽으로 이동한 경우
                str_1.append(str_2.pop())
        elif l == '-':
            if len(str_1) != 0:  # 백스페이스 하는 경우
                str_1.pop()
        else:
            str_1.append(l)

    str_2.reverse()
    result.append(str_1 + str_2)

for r in result:
    print(''.join(r))