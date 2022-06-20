import sys
from collections import deque

input = sys.stdin.readline


def solution(N, A):
    answer = 0
    seq = [1] * (N + 1)
    max = A[0]

    #for i in range(1, N):
    #    if A[i] > max:




    return answer


if __name__ == '__main__':
    # input
    N = int(input().rstrip())
    A = list(map(int, input().rstrip().split()))

    # output
    print(solution(N, A))
