def get_joltage(bank, k):
    n = len(bank)
    res = ''
    st = 0
    for i in range(k, 0, -1):
        lst = list((chr, -(st + i)) for i, chr in enumerate(bank[st:n-i+1]))
        c, idx = max(lst)
        res += c
        st = -idx + 1
    return int(res)
        
# PART 2
with open("input.txt") as file:
    tot = 0
    for bank in file.readlines():
        bank = bank.rstrip('\n')
        # PART 1
        # tot += get_joltage(bank, 2)

        # PART 2
        tot += get_joltage(bank, 12)
    print(tot)
        