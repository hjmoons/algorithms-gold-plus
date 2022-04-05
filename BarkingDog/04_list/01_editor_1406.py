import sys

input = sys.stdin.readline

str = list(input().rstrip())
n = int(input().rstrip())

cursor = len(str)

for i in range(n):
    cmd = input().rstrip().split()
    #print(str, i)
    if cmd[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1
    elif cmd[0] == 'D':
        if cursor == len(str):
            continue
        cursor += 1
    elif cmd[0] == 'B':
        if cursor == 0:
            continue
        elif cursor == len(str):
            #print(cursor, i)
            str.remove(str[cursor-1])
            cursor -= 1
        else:
            str.remove(str[cursor-1])
    elif cmd[0] == 'P':
        str.insert(cursor, cmd[1])

print(str)


