import sys
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()
        self.count = 0

    # 정수 X를 덱의 앞에 입력
    def push_front(self, x):
        self.items.appendleft(x)
        self.count += 1

    # 정수 X를 덱의 뒤에 입력
    def push_back(self, x):
        self.items.append(x)
        self.count += 1

    # 덱의 가장 앞에 있는 수를 빼고, 그 수 출력
    # 덱에 정수가 없는 경우 -1을 출력
    def pop_front(self):
        if self.count > 0:
            print(self.items.popleft())
            self.count -= 1
        else:
            print(-1)

    # 덱의 가장 뒤에 있는 수를 빼고, 그 수 출력
    # 덱에 정수가 없는 경우 -1 출력
    def pop_back(self):
        if self.count > 0:
            print(self.items.pop())
            self.count -= 1
        else:
            print(-1)

    # 덱에 있는 정수의 개수를 출력
    def size(self):
        print(self.count)

    # 덱이 비어 있으면 1 아니면 0 출력
    def empty(self):
        if self.count == 0: print(1)
        else: print(0)

    # 덱의 가장 앞에 있는 정수를 출력
    # 덱에 정수가 없는 경우 -1 출력
    def front(self):
        if self.count > 0:
            print(self.items[0])
        else:
            print(-1)

    # 덱의 가장 뒤에 있는 정수 출력
    # 덱에 정수가 없는 경우 -1 출력
    def back(self):
        if self.count > 0:
            print(self.items[self.count-1])
        else:
            print(-1)

    def command(self, cmd, param):
        if cmd == 'push_front':
            self.push_front(param)
        elif cmd == 'push_back':
            self.push_back(param)
        elif cmd == 'pop_front':
            self.pop_front()
        elif cmd == 'pop_back':
            self.pop_back()
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

s = Deque()

for c in cmds:
    if len(c) > 1:
        s.command(c[0], c[1])
    else:
        s.command(c[0], 0)