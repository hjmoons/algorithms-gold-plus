import sys
from itertools import combinations

def solution(T, N, books, values):
    answer = []

    for a in T:
        min_value = 1000000
        min_index = -1
        min_book = -1
        for i in range(N):
            if a in books[i]:
                index = books[i].index(a)
                min_index = index
                min_book = i
                if books[i] in answer:
                    min_value = values[i]
                    break
                min_value = min(min_value, values[i])

        books[min_book][min_index] = 0
        print(books[min_book])
        answer.append(min_value)

    return answer


if __name__ == '__main__':
    input = sys.stdin.readline

    T = list(input().rstrip())
    N = int(input().rstrip())
    values = []
    books = []
    for _ in range(N):
        a, b = input().rstrip().split()
        values.append(int(a))
        books.append(list(b))

    print(solution(T, N, books, values))
