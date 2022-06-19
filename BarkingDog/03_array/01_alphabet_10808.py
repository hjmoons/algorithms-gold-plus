import sys


def solution(S):
    answer = [0] * 26
    for c in S:
        answer[ord(c)-97] += 1
    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    S = input().rstrip()

    print(*solution(S))
