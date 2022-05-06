import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    func = input().rstrip()
    length = int(input().rstrip())
    arr = input().rstrip()

    # 입력된 배열을 데크로 전환
    arr_deq = []
    if length < 1:
        arr_deq = deque()
    else:
        arr_deq = deque(list(map(int, arr[1:-1].split(","))))

    # RD 함수 처리
    check = True    # 배열의 길이가 0인 경우 확인 변수
    reverse = False     # False 일 경우 왼쪽 팝, True일 경우 오른쪽 팝
    for f in func:
        if f == 'R':
            reverse = not reverse # reverse = not reverse
        elif f == 'D':
            # 배열의 길이가 0인 경우 팝 불가능 -> error
            if length < 1:
                check = False
                break

            # reverse 변수가 홀수일 경우 오른쪽팝, 짝수일 경우 왼쪽팝
            if reverse:
                arr_deq.pop()
            else:
                arr_deq.popleft()

            length -= 1

    if check:   # error 발생 여부 확인
        if length < 1:  # 배열의 길이가 0인 경우
            result.append("[]")
        else:
            if int(reverse%2):  # reverse 변수가 홀수일 경우 역순
                arr_deq.reverse()
            result.append(str(arr_deq)[6:-1].replace(" ", ""))
    else:
        result.append("error")

for r in result:
    print(r)