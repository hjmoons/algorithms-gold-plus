import sys

input = sys.stdin.readline

n = int(input().rstrip())
balloons = list(map(int, input().rstrip().split()))

check = [0] * 1000001   # 화살의 위치
count = 0               # 화살 수

for i in range(n):
    bal = balloons[i]

    # 현재 풍선 높이에 화살이 있는지 확인
    # 화살이 없는 경우 (0인 경우) -> 새로운 화살 발사, 현재 풍선 터뜨리고 1을 뺀 높이에 화살 표시
    # 화살이 있는 경우 (0이 아닌 경우) -> 현재 풍선을 터뜨리고 화살을 없앤 후(-1) 1을 뺀 높이에 화살 표시
    if check[bal] == 0:
        count += 1
        check[bal - 1] += 1
    else:
        check[bal] -= 1
        check[bal - 1] += 1

print(count)