
import re
from functools import reduce

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

# Part 1
with open("Day5/input.txt", "r") as my_file:
    lines = [x.strip() for x in my_file.readlines() if x.strip() != '']
    seeds = [int(x) for x in re.findall(r'(\d+)', lines[0].split("seeds: ")[1])]
    lines = lines[1:]
    res = list()
    maps = dict()
    val = -1
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
    for seed in seeds:
        for map in maps.values():
            for e in map:
                if seed >= e.source and seed <= (e.source + e.range):
                    seed = e.dest + abs(seed - e.source)
                    break
        if val < 0 or seed < val:
            val = seed
          
    print(val)
   
def process_range(seed_tuple):
    val = -1
    seed = seed_tuple[0]
    idx_end = seed_tuple[0] + seed_tuple[1]
    
    pid = os.getpid()
    start_seed = seed
    counter = 0
    print(f'start pid: {pid} on seed: {start_seed}\n')
    while seed <= idx_end:
        tmp_val = seed
        for map in maps.values():
            for e in map:
                if tmp_val >= e.source and tmp_val <= (e.source + e.range):
                    tmp_val = e.dest + abs(tmp_val - e.source)
                    break
        if val < 0 or tmp_val < val :
            val = tmp_val
        seed += 1
            
        counter += 1
        if counter % 1_000_000 == 0:
            print(f'pid: {pid} seed: {seed} left: {idx_end - seed} val: {val}\n')  
    return val

# not correct 6082853

import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
import os
global maps
# global g_val
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

    # interval = (max_val - min_val) // cpu_count
    # my_seed_list = list()
    # start_val = min_val
    # for i in range(cpu_count):
    #     my_seed_list.append((start_val, interval))
    #     start_val += interval
    
    results = list()
    # t1 = process_range(seed_tuple=seeds_tuples[0])
    # t2 = process_range(seed_tuple=seeds_tuples[1])
    with ProcessPoolExecutor(max_workers=workers) as executor:
        executor.submit(process_range, workers)
        results = executor.map(process_range, seeds_tuples)
    print(min(results))      
    # print(g_val.value)
