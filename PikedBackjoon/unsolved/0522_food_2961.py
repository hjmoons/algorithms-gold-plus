import sys


def solution(N, F):
    answer = 0
    score = 1000000000
    i = 0
    count = 1
    while i < N:
        if count == 1:
            answer = min(score, abs(F[i][0] - F[i][1]))
            print(i, count, answer)
            count += 1
        else:
            a = F[i][0]   # 신맛
            b = F[i][1]   # 단맛
            for j in range(i + 1, N):
                a *= F[j][0]
                b += F[j][1]
            answer = min(score, abs(a - b))
            print(i, count, answer)
            count += 1

        if count > N:
            i += 1
            count = i + 1

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input().rstrip())
    F = []
    for _ in range(N):
        F.append(list(map(int, input().rstrip().split())))

    print(solution(N, F))
