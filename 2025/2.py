# # PART 1
# with open("input.txt") as file:
#     for line in file.readlines():
#         ranges = [
#             (int(r.split('-')[0]), int(r.split('-')[1])) for r in line.split(',')
#         ]

#         # 2259304 values
#         cnt = 0
#         for l, r in ranges:
#             for x in range(l, r + 1):
#                 y = str(x)
#                 if len(y) % 2 == 0:
#                     k = int(len(y) / 2)
#                     a, b = y[:k], y[k:]
#                     cnt += int(y) if a == b else 0
#         print(cnt)


# PART 2
with open("input.txt") as file:
    for line in file.readlines():
        ranges = [
            (int(r.split('-')[0]), int(r.split('-')[1])) for r in line.split(',')
        ]

        # 2259304 values
        cnt = 0
        for l, r in ranges:
            for x in range(l, r + 1):
                y = str(x)
                for k in range(1, len(y)):
                    if (len(y) % k == 0):
                        s = set(y[i * k:(i + 1) * k] for i in range(0, len(y) // k))
                        if len(s) == 1:
                            cnt += x
                            break
        print(cnt)
