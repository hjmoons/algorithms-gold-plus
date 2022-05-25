import sys


def solution(s):
    answer = 0
    stack = []
    t = 1
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            t *= 2
        elif s[i] == '[':
            stack.append(s[i])
            t *= 3
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                answer = 0
                break
            if s[i-1] == '(':
                answer += t
            t //= 2
            stack.pop()
        else:
            if not stack or stack[-1] != '[':
                answer = 0
                break
            if s[i-1] == '[':
                answer += t
            t //= 3
            stack.pop()

    if stack:
        answer = 0

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    s = input().rstrip()

    print(solution(s))
