
import re
import copy
from number import Number
# 12 red cubes, 13 green cubes, and 14 blue cubes

#Part 1
res_dict = {}
mask_symbol = '!'
with open("Day3/test.txt", "r") as my_file:
    lines = my_file.readlines()
    y_max = len(lines) - 1
    x_max = len(lines[0]) - 2
    idx = 0
    m = []
    for line in lines:
        line = line.strip()   
        row = []

        for c in line:   
            row.append(c)
        m.append(row)    
m_masked = copy.deepcopy(m)   
for y_idx in range(y_max):
    for x_idx in range(x_max):
        c = m_masked[y_idx][x_idx]   
        if not c.isdigit() and (c != '.' and c != mask_symbol):
            if y_idx > 0 and x_idx > 0:
                m_masked[y_idx - 1][x_idx - 1] = mask_symbol
            if y_idx > 0:
                m_masked[y_idx - 1][x_idx] = mask_symbol
            if y_idx > 0 and x_idx < x_max:
                m_masked[y_idx - 1][x_idx + 1] = mask_symbol
            if x_idx > 0:
                m_masked[y_idx][x_idx - 1] = mask_symbol
            if x_idx < x_max:
                m_masked[y_idx][x_idx + 1] = mask_symbol
            if y_idx < y_max and x_idx > 0:
                m_masked[y_idx + 1][x_idx - 1] = mask_symbol
            if y_idx < y_max:
                m_masked[y_idx + 1][x_idx] = mask_symbol
            if y_idx < y_max and x_idx < x_max:
                m_masked[y_idx + 1][x_idx + 1] = mask_symbol

for row in m_masked:
    print(row)
print('\n-------------------------------------\n')
for row in m:
    print(row)    
    # for c in row:   
    #     print(c)

res = []
for y_idx in range(y_max):
    for x_idx in range(x_max):
        x_copy = x_idx
        c_masked = m_masked[y_idx][x_idx]
        c = m[y_idx][x_idx]
        if c_masked == mask_symbol and c.isdigit():
            tmp_str = str(c)
            x_copy -= 1
            while x_copy > -1 or not c.isdigit():
                c = m[y_idx][x_copy]
                if c == '.':
                    break
                if c.isdigit():
                    tmp_str = c + tmp_str
                x_copy -= 1
            
            c = m[y_idx][x_idx]
            x_copy = x_idx
            x_copy += 1
            while x_copy <= x_max or not c.isdigit():
                c = m[y_idx][x_copy]
                if c == '.':
                    break
                if c.isdigit():
                    tmp_str = tmp_str + c
                x_copy += 1
            res.append(int(tmp_str))
            
print(sum(res))

        
