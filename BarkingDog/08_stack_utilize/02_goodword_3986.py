import sys

input = sys.stdin.readline


def solution(words):
    answer = 0

    for word in words:

        stack = []
        count = 0
        check = True

        for i in range(len(word)):
            print(stack, word[i])
            if count < 1:
                stack.append(word[i])
                count += 1
                continue

            if word[i] == stack[count - 1]:
                stack.pop()
                count -= 1
            else:
                stack.append(word[i])


        if not stack:
            answer += 1


    return answer


if __name__ == '__main__':
    words = []
    # input
    N = int(input().rstrip())
    for _ in range(N):
        words.append(input().rstrip())

    print(solution(words))
