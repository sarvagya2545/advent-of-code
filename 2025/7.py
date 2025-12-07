grid = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        grid.append(line.rstrip('\n'))

beams = set()
for idx in range(0, len(grid[0])):
    if grid[0][idx] == 'S':
        beams.add(idx)

timelines_count = [0] * len(grid[0])
for idx in beams:
    timelines_count[idx] = 1

split_count = 0
for row in range(1, len(grid)):
    splitters = [idx for idx in range(0, len(grid[row])) if grid[row][idx] == '^']
    new_timelines_count = timelines_count
    for split in splitters:
        if split in beams:
            split_count += 1
            beams.remove(split)
            beams.add(split + 1)
            beams.add(split - 1)
            x = new_timelines_count[split]
            new_timelines_count[split] = 0
            new_timelines_count[split - 1] += x
            new_timelines_count[split + 1] += x
    timelines_count = new_timelines_count

# PART 1
print(split_count)

# PART 2
print(sum(timelines_count))