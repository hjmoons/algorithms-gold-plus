import sys
from collections import deque

input = sys.stdin.readline


def solution(N):
    answer = deque(range(1, N + 1))

    while len(answer) != 1:
        answer.popleft()
        if len(answer) == 1:
            break

        answer.append(answer.popleft())

    return answer[0]


if __name__ == '__main__':
    # input
    N = int(input().rstrip())

    # output
    print(solution(N))
