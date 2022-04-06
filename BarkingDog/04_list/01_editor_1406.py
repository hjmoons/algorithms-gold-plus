import sys

input = sys.stdin.readline

str_1 = list(input().rstrip())  # 커서 왼쪽
str_2 = []  # 커서 오른쪽

n = int(input().rstrip())

for i in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == 'L' and len(str_1) != 0:
        str_2.append(str_1.pop())
    elif cmd[0] == 'D' and len(str_2) != 0:
        str_1.append(str_2.pop())
    elif cmd[0] == 'B' and len(str_1) != 0:
        str_1.pop()
    elif cmd[0] == 'P':
        str_1.append(cmd[1])

str_2.reverse() # str_2에서 팝을 해야 정상 순서이므로 역순으로 출력
print(''.join(str_1 + str_2))