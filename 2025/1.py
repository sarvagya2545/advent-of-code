
# PART 1
with open("input.txt", 'r') as file:
    cur = 50
    cnt = 0
    for line in file.readlines():
        dir = -1 if line[0] == 'L' else 1
        num = int(line[1:]) * dir
        cur = (cur + num + 100) % 100
        if cur == 0:
            cnt += 1

    print(cnt)

# PART 2
with open("input.txt", 'r') as file:
    cur = 50
    cnt = 0
    for line in file.readlines():
        num = int(line[1:])
        if num >= 100:
            cnt += num // 100
            num = num % 100
        dir = -1 if line[0] == 'L' else 1
        num *= dir
        nxt = cur + num
        if (nxt <= 0 and cur - 1 >= 0) or (cur + 1 <= 100 and nxt >= 100):
            cnt += 1
        cur = (nxt + 100) % 100

    print(cnt)