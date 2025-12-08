from typing import Tuple, List
from heapq import heappop, heappush

points: List[Tuple[int, int, int]] = []

with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        x, y, z = line.split(',')
        points.append((int(x), int(y), int(z)))

n = len(points)
min_heap = []
dist = lambda i, j: sum((points[i][dim] - points[j][dim]) ** 2 for dim in range(3))

MAX_POINTS_SIZE = 1000

for i in range(0, n):
    for j in range(i + 1, n):
        heappush(min_heap, (-dist(i, j), i, j))
        if len(min_heap) > MAX_POINTS_SIZE:
            heappop(min_heap)

graph = [[] for _ in range(0, n)]
for _, u, v in sorted(min_heap, key=lambda x: -x[0]):
    graph[u].append(v)
    graph[v].append(u)


visited = [0] * n
def dfs(node, label):
    visited[node] = label
    for next in graph[node]:
        if not visited[next]:
            dfs(next, label)

label = 1
for node in range(0, n):
    if not visited[node]:
        dfs(node, label)
        label += 1

cnts = [0] * label
for label in visited:
    cnts[label] += 1

ans = 1
for x in sorted(cnts, reverse=True)[:3]:
    ans *= x

print(ans)