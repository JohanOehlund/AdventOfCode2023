
import re
from functools import reduce
import math
def f(t, d):
    x0 =  math.floor((t / 2) - math.sqrt(math.pow(-(t/2), 2) - d))
    x1 =  math.ceil((t / 2) + math.sqrt(math.pow(-(t/2), 2) - d))
    return x0, x1

# Part 1
with open("Day6/input2.txt", "r") as my_file:
    lines = [x.strip() for x in my_file.readlines() if x.strip() != '']
    times = [int(x) for x in re.findall(r'(\d+)', lines[0].split(":")[1])]
    distances = [int(x) for x in re.findall(r'(\d+)', lines[1].split(":")[1])]
    races = list(zip(times, distances))
    result_list = []
    for race in races:
        t = race[0]
        d = race[1]
        x0, x1 = f(t, d)
        result_list.append(abs(x1- x0) - 1)
    result = reduce((lambda x, y: x * y), result_list)
    pass
    # t = T - B
    # D = t * B 
    # D = (T - B) * B 
    # B^2 - T*B + D = 0 
    # x = t/2 + sqrt(-(t/2)² - d)
