from typing import List

def rotate(grid: List[List[any]]) -> List[List[any]]:
    m = len(grid)
    n = len(grid[0])
    # grid[i][j] -> newgrid[m - j][i]
    newgrid = [[None for _ in range(0, m)] for _ in range(0, n)]

    for i in range(0, m):
        for j in range(0, n):
            newgrid[n - j - 1][i] = grid[i][j]
    return newgrid


if __name__ == '__main__':
    grid = []
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            grid.append(line.rstrip('\n'))
    grid = rotate(grid)

    ans = 0

    s = 0
    p = 1
    for row in grid:
        row = ''.join(row).rstrip(' ')
        if len(row) == 0:
            s = 0
            p = 1
        else:
            num = int(row.rstrip('+').rstrip('*'))
            s += num
            p *= num

        if row != '' and row[-1] in ['+', '*']:
            ans += s if row[-1] == '+' else p
    print(ans)