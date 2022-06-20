import sys

input = sys.stdin.readline

n = int(input().rstrip())
balloons = list(map(int, input().rstrip().split()))

check = [0] * 1000001   # 화살의 위치 ( n+1로 했는데 런타임 에러 발생 -> 1000001로 변경)
count = 0               # 화살 수

for i in range(n):
    bal = balloons[i]

    # 현재 풍선 높이에 화살이 있는지 확인
    if check[bal] == 0:         # 화살이 없는 경우 (0인 경우) -> ,
        count += 1              # 새로운 화살 발사
        check[bal - 1] += 1     # 현재 풍선 터뜨리고 1을 뺀 높이에 화살 표시
    else:                       # 화살이 있는 경우 (0이 아닌 경우) ->
        check[bal] -= 1         # 현재 풍선을 터뜨리고 화살 이동
        check[bal - 1] += 1     # 화살의 높이를 1 줄인 위치에 화살 표시

print(count)