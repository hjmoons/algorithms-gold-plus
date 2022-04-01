import sys

class Stack:
    def __init__(self):
        self.items = []
        self.count = 0

    # 정수 X를 스택에 넣는 연산
    def push(self, x):
        self.items.append(x)
        self.count += 1

    # 스택에서 가장 위에 있는 정수를 뺴고, 수 출력
    # 스택에 들어있는 정수가 없는 경우 -1 출력
    def pop(self):
        if self.count != 0:
            print(self.items.pop())
            self.count -= 1
        else:
            print(-1)

    # 스택에 들어있는 정수의 개수 출력
    def size(self):
        print(self.count)

    # 스택이 비어있으면 1, 아니면 0 출력
    def empty(self):
        if self.count == 0: print(1)
        else: print(0)

    # 스택의 가장 위에 있는 정수 출력
    # 스택에 들어있는 정수가 없는 경우 -1 출력
    def top(self):
        if self.count != 0:
            print(self.items[self.count-1])
        else:
            print(-1)

    def stackCommand(self, cmd, param):
        if cmd == 'push':
            self.push(param)
        elif cmd == 'pop':
            self.pop()
        elif cmd == 'size':
            self.size()
        elif cmd == 'empty':
            self.empty()
        elif cmd == 'top':
            self.top()

input = sys.stdin

cmds = []
n = int(input.readline().strip())
for i in range(n):
    s = input.readline().strip().split()
    cmds.append(s)

s = Stack()

for c in cmds:
    if len(c) > 1:
        s.stackCommand(c[0], c[1])
    else:
        s.stackCommand(c[0], 0)