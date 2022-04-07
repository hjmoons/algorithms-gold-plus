import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
road = defaultdict(dict)

for _ in range(8):
    a, b, c = map(int, input().rstrip().split())
    road[a][b] = c

print(road)