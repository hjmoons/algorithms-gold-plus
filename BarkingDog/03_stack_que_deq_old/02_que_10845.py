import sys
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
        self.count = 0

    # 정수 X를 큐에 넣는 연산
    def push(self, x):
        self.items.append(x)
        self.count += 1

    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수 출력
    # 큐에 정수가 없는 경우 -1 출력
    def pop(self):
        if self.count > 0:
            print(self.items.popleft())
            self.count -= 1
        else:
            print(-1)

    # 큐에 있는 정수의 개수를 출력
    def size(self):
        print(self.count)

    # 큐가 비어 있으면 1 아니면 0 출력
    def empty(self):
        if self.count == 0: print(1)
        else: print(0)

    # 큐의 가장 앞에 있는 정수를 출력
    # 큐에 정수가 없는 경우 -1 출력
    def front(self):
        if self.count > 0:
            print(self.items[0])
        else:
            print(-1)

    # 큐의 가장 뒤에 있는 정수 출력
    # 만약 큐에 정수가 없는 경우 -1 출력
    def back(self):
        if self.count > 0:
            print(self.items[self.count-1])
        else:
            print(-1)

    def command(self, cmd, param):
        if cmd == 'push':
            self.push(param)
        elif cmd == 'pop':
            self.pop()
        elif cmd == 'size':
            self.size()
        elif cmd == 'empty':
            self.empty()
        elif cmd == 'front':
            self.front()
        elif cmd == 'back':
            self.back()

input = sys.stdin

cmds = []   # 입력 명령어 리스트

# Input
n = int(input.readline().strip())
for i in range(n):
    s = input.readline().strip().split()
    cmds.append(s)

s = Queue()

for c in cmds:
    if len(c) > 1:
        s.command(c[0], c[1])
    else:
        s.command(c[0], 0)