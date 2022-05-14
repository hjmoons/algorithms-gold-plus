import sys

input = sys.stdin.readline


def solution(string):
    answer = 'yes'
    dc = {')': '(', '}': '{', ']': '['}  # 괄호 매핑
    op = dc.values()    # 열린 괄호
    cl = dc.keys()    # 닫힌 괄호
    stack = []
    count = 0

    for i in range(len(string)):
        if count == 0 and string[i] in cl:
            answer = 'no'
            break
        elif string[i] in op:
            stack.append(string[i])
            count += 1
        elif string[i] in cl:
            if dc[string[i]] == stack[count-1]:
                stack.pop()
                count -= 1
            else:
                answer = 'no'
                break
        elif string[i] == '.' and count > 0:
            answer = 'no'
            break

    return answer


if __name__ == '__main__':
    # input
    while True:
        string = input().rstrip()
        if string == '.':
            break
        print(solution(string))
