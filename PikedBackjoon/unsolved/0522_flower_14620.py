import sys


def solution(G):
    answer = 0
    value = []
    seed = 1

    while seed < 4:

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    G = []
    for i in range(N):
        G.append(list(map(int, input().rstrip().split())))

    print(solution(G))
