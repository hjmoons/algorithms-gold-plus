import sys


def solution(words):
    answer = 0

    for word in words:

        stack = []
        count = 0

        for i in range(len(word)):
            if count < 1:
                stack.append(word[i])
                count += 1
                continue

            if word[i] == stack[count - 1]:
                stack.pop()
                count -= 1
            else:
                stack.append(word[i])
                count += 1

        if not stack:
            answer += 1

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    words = []
    # input
    N = int(input().rstrip())
    for _ in range(N):
        words.append(input().rstrip())

    print(solution(words))
