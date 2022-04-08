import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
road = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    road[a].append([b, c])
    road[b].append([a, c])

INF = int(1e9)
weight = [INF] * (n + 1)        # 1에서 시작했을 때 각 노드까지 가는 최소 여물

def dijkstra(start):
    q = []
    # 시작 노드 정보 힙큐에 입력
    heapq.heappush(q, (0, start))
    weight[start] = 0
    while q:
        w, node = heapq.heappop(q)
        # 힙큐에서 꺼낸 여물의 크기가 새로운 경로의 여물의 크기 보다 작으면 다음 경로 확인
        if weight[node] < w:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in road[node]:
            cost = weight[node] + next[1]   # 시작->node거리 + node->node의인접노드 거리
            if cost < weight[next[0]]:      # cost < 시작->node의인접노드 거리
                weight[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(1)
print(weight[n])