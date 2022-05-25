import sys


def solution(sticks):
    answer = 0
    sticks = sticks.replace("()", "*")
    stack = []

    for i in range(len(sticks)):
        if sticks[i] == '(':        # 쇠막대기 시작
            stack.append(sticks[i])
        elif sticks[i] == ')':      # 쇠막대기 끝
            stack.pop()
            answer += 1
        else:   # 레이저일 경우
            answer += len(stack)

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    sticks = input().rstrip()

    print(solution(sticks))
