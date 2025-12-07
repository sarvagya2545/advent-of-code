grid = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        grid.append(line.rstrip('\n'))

beams = set()
for idx in range(0, len(grid[0])):
    if grid[0][idx] == 'S':
        beams.add(idx)

split_count = 0
for row in range(1, len(grid)):
    splitters = [idx for idx in range(0, len(grid[row])) if grid[row][idx] == '^']
    for split in splitters:
        if split in beams:
            split_count += 1
            beams.remove(split)
            beams.add(split + 1)
            beams.add(split - 1)

print(split_count)