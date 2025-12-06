import copy
from typing import List, Union, Tuple

def parse_line(line: str) -> List[Union[int, str]]:
    # Split and remove empty strings
    items = list(filter(lambda x: x != '', line.split(' ')))
    if items[0][0] >= '0' and items[0][0] <= '9':
        # Turn everything to ints
        items = list(map(lambda x: int(x), items))
    return items


def process_item(result_item: Tuple[int, int], item: int) -> Tuple[int, int]:
    return (result_item[0] + item, result_item[1] * item)


def process(result: List[Tuple[int, int]], items: List[int]) -> List[Tuple[int, int]]:
    return list(map(lambda x: process_item(*x), zip(result, items)))


def get_answer(result: List[Tuple[int, int]], items: List[str])->int:
    return sum((result_item[0] if operation == '+' else result_item[1]) 
                for result_item, operation in zip(result, items))


with open("input.txt", 'r') as file:
    result: List[Tuple[int, int]] = []
    for line in file.readlines():
        line = line.rstrip('\n')
        items = parse_line(line)
        if items[0] in ['*', '+']:
            print(get_answer(result, items))
        else:
            if len(result) == 0:
                result = [(0, 1)] * len(items)
            result = process(result, items)