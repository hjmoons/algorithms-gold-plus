import sys

input = sys.stdin.readline

n = int(input().rstrip())
tops = list(map(int, input().rstrip().split()))
stack = []  # 높이 스택
i_stack = []  # 인덱스 스택
st = -1  # 스택의 탑
answer = []  # 결과값 리스트

for i in range(n):
    # 첫 탑은 아무 신호도 수신하지 않음
    if i == 0:
        stack.append(tops[i])  # 스택에 탑의 높이와 위치를 삽입
        i_stack.append(i + 1)
        answer.append(i)  # 결과에 아무것도 받지 않으므로 0 삽입
        st += 1
        continue

    # 두번째 탑 부터는 앞의 탑으로부터 신호 수신 가능
    # 스택을 팝하면서 최상단과 현재 탑의 높이를 비교
    while st > -1:
        if stack[st] > tops[i]:  # 스택의 최상단이 크면 수신하는 탑이 됨 -> 반복문 중단
            break

        stack.pop()
        i_stack.pop()
        st -= 1

    if st > -1:  # 스택에 수가 존재하면 최상단의 인덱스를 결과에 삽입
        answer.append(i_stack[st])
    else:  # 그렇지 않으면 수신하는 탑이 없으므로 0 삽입
        answer.append(0)

    # 스택의 현재 탑의 높이와 인덱스 삽입
    stack.append(tops[i])
    i_stack.append(i + 1)
    st += 1

for a in answer:
    print("{0} ".format(a), end='')
