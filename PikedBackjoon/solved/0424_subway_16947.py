import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
subway = defaultdict(list)
visited = [0] * (N + 1)

for _ in range(N):
    s1, s2 = map(int, input().strip().split())
    subway[s1].append(s2)


def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.popleft()

        ##만약 방문한 리스트에 없다면
        if node not in visited:

            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return need_visited


print(dfs2(subway, 1))