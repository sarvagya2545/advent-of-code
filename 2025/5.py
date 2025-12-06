from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    merged_intervals = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for l, r in sorted_intervals:
        if len(merged_intervals) == 0 or merged_intervals[-1][1] < l:
            merged_intervals.append((l, r))
        else:
            merged_intervals[-1] = min(l, merged_intervals[-1][0]), max(merged_intervals[-1][1], r)
    return merged_intervals


def is_item_present_in_intervals(item: int, intervals: List[Tuple[int,int]]) -> List[Tuple[int, int]]:
    left = 0
    right = len(intervals) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        l = intervals[mid][0]
        if item >= l:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    if ans == -1:
        return False
    
    l, r = intervals[ans]
    return item >= l and item <= r


with open("input.txt", "r") as file:
    intervals = []
    items = []
    get_items = False
    for line in file.readlines():
        line = line.rstrip('\n')

        if line == '':
            get_items = True
            continue
        
        if get_items:
            items.append(int(line))
        else:
            l, r = line.split('-')
            intervals.append((int(l), int(r)))

    intervals = merge_intervals(intervals)

    count = 0
    for item in items:
        if is_item_present_in_intervals(item, intervals):
            count += 1
    print(count)