import sys
from collections import deque

input = sys.stdin.readline


def solution(X):
    answer = 0

    count = [0] * (X + 1)
    results = deque(X)
    i = 0

    while results:
        i += 1
        n = results.popleft()
        if n % 3 == 0:
            r = int(n/3)
            if count[r] > i:
                count[r] = i

        if n % 2 == 0:
            r = int(n/2)
            count[r] = i



    return answer


if __name__ == '__main__':
    # input
    X = int(input().rstrip())

    # output
    print(solution(X))
