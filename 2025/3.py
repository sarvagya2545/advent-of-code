# PART 1
with open("input.txt") as file:
    tot = 0
    for bank in file.readlines():
        mx = 0
        cur_mx = ord(bank[-1]) - ord('0')
        for i in range(len(bank) - 2, -1, -1):
            num = ord(bank[i]) - ord('0')
            mx = max(mx, num * 10 + cur_mx)
            cur_mx = max(cur_mx, num)
        tot += mx
    print(tot)
        