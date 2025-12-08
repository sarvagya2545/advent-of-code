from typing import Tuple, List
from heapq import heappop, heappush

points: List[Tuple[int, int, int]] = []

with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        x, y, z = line.split(',')
        points.append((int(x), int(y), int(z)))

n = len(points)

# PART 1
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

# PART 2
class DSU:
    def __init__(self, n):
        self.par = [None] * n
        self.wt = [1] * n
        for i in range(0, n):
            self.par[i] = i
    
    def join(self, u, v):
        u = self.root(u)
        v = self.root(v)
        
        if u == v:
            return

        if self.wt[u] > self.wt[v]:
            tmp = u
            u = v
            v = tmp
        
        self.par[u] = v

    def root(self, x):
        if self.par[x] == x:
            return x
        return self.root(self.par[x])

    def is_connected(self, u, v):
        return self.root(u) == self.root(v)


distances: List[Tuple[int, int, int]] = []
for i in range(0, n):
    for j in range(i + 1, n):
        distances.append((dist(i, j), i, j))

dsu = DSU(n)
connected_components_count = n
for _, i, j in sorted(distances):
    if not dsu.is_connected(i, j):
        dsu.join(i, j)
        connected_components_count -= 1
    if connected_components_count == 1:
        print(points[i][0] * points[j][0])
        break