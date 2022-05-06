import sys
from collections import deque

input = sys.stdin.readline


def solution(N, commands):
    answer = []

    items = deque()
    count = 0

    for cmd in commands:
        c = cmd.split()
        if c[0] == 'push':
            items.append(c[1])
            count += 1
        elif c[0] == 'pop':
            item = -1
            if count > 0:
                item = items.popleft()
                count -= 1
            print(item)
        elif c[0] == 'size':
            print(count)
        elif c[0] == 'empty':
            print(1 if count == 0 else 0)
        elif c[0] == 'front':
            print(items[0] if count > 0 else -1)
        elif c[0] == 'back':
            print(items[count-1] if count > 0 else -1)

    return answer


if __name__ == '__main__':
    # input
    N = int(input().rstrip())
    commands = []
    for _ in range(N):
        commands.append(input().rstrip())

    # output
    #print(solution(N, commands))
    solution(N, commands)
