
import re
import copy
from number import Number
from symbol import Symbol
from functools import reduce
# 12 red cubes, 13 green cubes, and 14 blue cubes

#Part 1
# with open("Day3/input.txt", "r") as my_file:
#     lines = my_file.readlines()
#     numbers = list()
#     symbols = list()
#     y = 0
#     for line in lines:
#         line = line.strip()
#         for m in re.finditer(r'[^.\d]',line):
#             symbols.append(Symbol(m.start(), y, m.group()))
#         for m in re.finditer(r'(\d+)',line):
#             numbers.append(Number(m.start(), m.end() - 1, y, m.group()))
#         y += 1
    
#     res_list = list()
#     for number in numbers:
#         if number.has_adjacent_symbol(symbols):
#             res_list.append(int(number.num))

#     print(sum(res_list))

# Part 2
with open("Day3/input.txt", "r") as my_file:
    lines = my_file.readlines()
    numbers = list()
    symbols = list()
    y = 0
    for line in lines:
        line = line.strip()
        for m in re.finditer(r'[*]',line):
            symbols.append(Symbol(m.start(), y, m.group()))
        for m in re.finditer(r'(\d+)',line):
            numbers.append(Number(m.start(), m.end() - 1, y, m.group()))
        y += 1
    
    res_list = list()
    for symbol in symbols:
        nums = symbol.is_gear_symbol(numbers)
        if len(nums) > 1:
            test = reduce((lambda x, y: int(x.num) * int(y.num)), nums)
            res_list.append(test)

    print(sum(res_list))


