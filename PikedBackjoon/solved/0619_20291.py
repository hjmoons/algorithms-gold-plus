import sys


def solution(N, files):
    answer = {}

    for name, ext in files:
        if ext not in answer:
            answer[ext] = 1
        else:
            answer[ext] += 1

    return sorted(answer.items())


if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input().rstrip())
    files = [input().rstrip().split('.') for _ in range(N)]

    for key, value in solution(N, files):
        print(key, value)
