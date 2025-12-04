# PART 1
with open("input.txt", "r") as file:
    grid = []
    for row in file.readlines():
        row = row.rstrip('\n')
        grid.append(row)
    
    m = len(grid)
    n = len(grid[0])

    dirs = [
        (di, dj) 
        for di in range(-1, 2) 
            for dj in range(-1, 2) 
                if not (di == 0 and dj == 0)
    ]

    ans = 0
    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == '.':
                continue
            cnt = 0
            for di, dj in dirs:
                if i + di < 0 or i + di >= m: continue
                if j + dj < 0 or j + dj >= n: continue
                cnt += grid[i + di][j + dj] == '@'
            if cnt < 4:
                ans += 1
    print(ans)

# PART 2
from queue import Queue

with open("input.txt", "r") as file:
    grid = []
    for row in file.readlines():
        row = row.rstrip('\n')
        grid.append(row)
    
    m = len(grid)
    n = len(grid[0])

    dirs = [
        (di, dj) 
        for di in range(-1, 2) 
            for dj in range(-1, 2) 
                if not (di == 0 and dj == 0)
    ]

    visited = [[0 for j in range(0, n)] for i in range(0, m)]

    def check(i, j) -> bool:
        cnt = 0
        for di, dj in dirs:
            if i + di < 0 or i + di >= m: continue
            if j + dj < 0 or j + dj >= n: continue
            cnt += grid[i + di][j + dj] == '@' and visited[i + di][j + dj] == 0
        return cnt < 4

    q = Queue()
    for i in range(0, m):
        for j in range(0, n):
            if grid[i][j] == '.':
                continue
            if check(i, j):
                q.put((i, j))
                visited[i][j] = 1

    while not q.empty():
        i, j = q.get()
        for di, dj in dirs:
            if i + di < 0 or i + di >= m: continue
            if j + dj < 0 or j + dj >= n: continue
            if visited[i + di][j + dj] == 1 or grid[i + di][j + dj] == '.':
                continue
            if check(i + di, j + dj):
                q.put((i + di, j + dj))
                visited[i + di][j + dj] = 1
    
    ans = sum(sum(row) for row in visited)
    print(ans)