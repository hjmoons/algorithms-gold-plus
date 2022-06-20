import sys
import copy


def solution(n, d, X):
    pre = X
    answer = copy.deepcopy(pre)
    mid = (n+1)//2 - 1
    rotate = (abs(d) // 45) % 8 # 회전수
    d_check = True  # 반시계: 0, 시계: 1
    if d < 0: d_check = False

    for _ in range(rotate):
        if d_check:
            '''
            X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
            X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
            X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
            X의 가운데 행을 X의 주 대각선으로 옮긴다.
            위 네 가지 경우 모두 원소의 기존 순서는 유지 되어야 한다.
            X의 다른 원소의 위치는 변하지 않는다.
            '''
            for i in range(n):
                answer[i][mid] = pre[i][i]
                answer[i][n-1-i] = pre[i][mid]
                answer[mid][i] = pre[n-1-i][i]
                answer[i][i] = pre[mid][i]
        else:
            for i in range(n):
                answer[i][mid] = pre[i][n-1-i]
                answer[i][i] = pre[i][mid]
                answer[mid][i] = pre[i][i]
                answer[n-1-i][i] = pre[mid][i]

        pre = answer
        answer = copy.deepcopy(pre)

    return answer


def print_(X):
    for i in X:
        print(*i)


if __name__ == '__main__':
    input = sys.stdin.readline

    T = int(input().rstrip())

    for _ in range(T):
        n, d = map(int, input().rstrip().split())
        X = [input().rstrip().split() for _ in range(n)]
        print_(solution(n, d, X))

