import sys


def solution(s):
    answer = 0
    stack = []
    top = -1
    t = 1
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
            top += 1
        elif stack[top] == '(' and (s[i] == '(' or s[i] == '['):
            stack.append(s[i])
            t *= 2
        elif stack[top] == '[' and (s[i] == '(' or s[i] == '['):
            stack.append(s[i])
            t *= 3

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    s = input().rstrip()

    print(solution(s))
