import sys

input = sys.stdin.readline


def solution(N, steps):
    answer = 0
    dp = [[0] * (N + 1)] * (N + 1)

    i = 0
    j = 0
    check = 0    # 3연속인지 확인

    while i < 6:
        if i == 0:
            dp[i][j] += steps[i]
            check += 1
            i += 1
            continue

        if check < 2:
            dp[i][j] = dp[i-1][j] + steps[i]
            check += 1
            i += 1
        else:
            print(i, j)
            j += 1
            dp[i][j] = dp[i-2][j] + steps[i]
            i += 1
            check = 0



    for d in dp:
        print(d)


    return answer


if __name__ == '__main__':
    # input
    N = int(input().rstrip())
    steps = [int(input().rstrip()) for _ in range(N)]

    print(solution(N, steps))
