import sys
from math import pow

input = sys.stdin.readline

# 입력
N = int(input().rstrip())
result = list(map(int, input().rstrip().split()))

# 카드 더미
cards = list(range(1, N + 1))

# N까지 나올 수 있는 K의 최대값
k_max = 0
while pow(2, k_max) < N:
    k_max += 1


# 카드 섞기 함수
def shuffle(c, k):
    card_list = c
    bottom = []     # 단계가 지날수록 뒤에 고정되는 수
    final = []      # 카드 섞기 마지막 최종 결과

    # 카드 섞기는 (2, K)일 경우 K+1까지 실행됨
    for i in range(1, k + 2):
        p = int(pow(2, k - i + 1))  # 2^k-i+1
        top = card_list[p * -1:]
        bottom = card_list[:len(card_list) - p] + bottom    # 단계가 지날수록 앞으로 옮긴 수 외의는 리스트의 뒤에 고정
        final = top + bottom
        card_list = top     # top외에는 bottom에 고정되어 있으므로 다음 단계에서는 top만 보면 됨

    return final


# 첫번째, 두번째 K값만 찾으면 되므로 k * k번 반복
check = False
for k in range(1, k_max):
    cards_1 = shuffle(cards, k)

    for l in range(1, k_max):
        cards_2 = shuffle(cards_1, l)

        if cards_2 == result:
            print(k, l)
            check = True
            break

    if check:
        break
