
import re
from functools import reduce
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
import os
global maps

class MapEntry:
    def __init__(self, dest, source, range):
        self.dest = dest
        self.source = source
        self.range = range

def create_map(lines):
    res = list()
    for idx, line in enumerate(lines):
        nums = [int(x) for x in re.findall(r'\d+', line)]
        if len(nums) >= 3:
            s = nums[1]
            d = nums[0]
            r = nums[2]
            m = MapEntry(d, s, r)
            res.append(m)
        else:
            break
    return res

# Part 2
with open("Day5/input.txt", "r") as my_file:
    lines = [x.strip() for x in my_file.readlines() if x.strip() != '']
    seeds_tuples = [(int(x[0]), int(x[1])) \
                    for x in re.findall(r'(\d+)\s+(\d+)', lines[0].split("seeds: ")[1])]
    seeds_tuples.sort()
    res = list()
    maps = dict()
    val = -1
    min_val = min(seeds_tuples)[0]
    max_val = max(seeds_tuples)[0] + max(seeds_tuples)[1]
    # g_val = mp.Value('l', max_val)   
    workers = len(seeds_tuples)
    # cpu_count = 1
    print("Number of workers : ", workers)


    for idx, line in enumerate(lines):
        if line.startswith("seed-to-soil"):
            maps[0] = create_map(lines[idx + 1:])
        elif line.startswith("soil-to-fertilizer"):
            maps[1] = create_map(lines[idx + 1:])
        elif line.startswith("fertilizer-to-water"):
            maps[2] = create_map(lines[idx + 1:])       
        elif line.startswith("water-to-light"):
            maps[3] = create_map(lines[idx + 1:])
        elif line.startswith("light-to-temperature"):
            maps[4] = create_map(lines[idx + 1:])
        elif line.startswith("temperature-to-humidity"):
            maps[5] = create_map(lines[idx + 1:])
        elif line.startswith("humidity-to-location"):
            maps[6] = create_map(lines[idx + 1:])
    i = 0
    val = -1
    found = False
    counter = 0
    while not found and i <= max_val:
        tmp_val = i
        start_val = i
        for map in reversed(maps.values()):
            for e in reversed(map):
                if tmp_val >= e.dest and tmp_val <= (e.dest + e.range):
                    tmp_val = e.source + abs(tmp_val - e.dest)
                    break
        for seed in seeds_tuples:
            if tmp_val >= seed[0] and tmp_val <= seed[0] + seed[1]:
                found = True
                val = start_val
                print(f'Finished: seed: {val}')
                break
        counter += 1
        if counter % 1_000_000 == 0:
            print(f'seed: {i} left: {max_val - i} val: {val}\n')              
        i += 1
