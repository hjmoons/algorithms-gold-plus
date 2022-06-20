import sys


def solution(N, h):
    answer = [-1] * N

    for i in range(N):
        k = 1
        for j in range(N):
            if h[i][0] < h[j][0] and h[i][1] < h[j][1]:
                k += 1
        answer[i] = k

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input().rstrip())
    h = [list(map(int, input().rstrip().split())) for _ in range(N)]

    print(*solution(N, h))
