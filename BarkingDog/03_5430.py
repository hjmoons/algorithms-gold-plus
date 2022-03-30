import sys
from collections import deque
input = sys.stdin

n = int(input.readline().strip())
result = []
for i in range(n):
    func = input.readline().strip()
    length = int(input.readline().strip())
    arr = input.readline().strip()
    if length < 1:
        arr = []
    else:
        arr = list(map(int, arr[1:-1].split(",")))

    arr_deq = deque(arr)
    check = True
    for f in func:
        if f == 'R':
            arr.reverse()
        elif f == 'D':
            if length < 1:
                check = False
                break
            arr = arr[1:]
            length -= 1

    if check:
        result.append(arr)
    else:
        result.append('error')

for r in result:
    print(str(r).replace(" ", ""))
