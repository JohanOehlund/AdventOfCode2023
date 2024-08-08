
import re
# 12 red cubes, 13 green cubes, and 14 blue cubes

#Part 1
# res_dict = {}
# with open("Day2/input.txt", "r") as my_file:
#     lines = my_file.readlines()
#     for line in lines:
#         line = line.strip()
#         tmp = re.match(r'Game (\d+)', line)
#         game_num = int(tmp.group(1))
#         red = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+red', line))))
#         green = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+green', line))))
#         blue = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+blue', line))))
#         if red <= 12 and green <= 13 and blue <= 14:
#             res_dict[game_num] = (red, green, blue)
            
# print(sum(res_dict.keys()))

#Part 2
res_dict = {}
with open("Day2/input.txt", "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        line = line.strip()
        tmp = re.match(r'Game (\d+)', line)
        game_num = int(tmp.group(1))
        red = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+red', line))))
        green = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+green', line))))
        blue = max(list(map(lambda x: int(x), re.findall(r'(\d+)\s+blue', line))))
        res_dict[game_num] = (red * green * blue)
            
print(sum(res_dict.values()))

        
