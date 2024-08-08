
import re
# # Part 1
# with open("Day4/input.txt", "r") as my_file:
#     lines = my_file.readlines()
#     res_list = list()
#     for line in lines:
#         line = line.strip()
#         num_left = re.findall(r'\d+', line.split(":")[1].split('|')[0])
#         num_right = re.findall(r'\d+', line.split(":")[1].split('|')[1])
#         matches_count = len(set(num_left) & set(num_right))
#         res = 0
#         for i in range(matches_count):
#             if i == 0:
#                 res = 1
#             else:
#                 res *= 2
#         res_list.append(res)
# print(sum(res_list))

# Part 2
with open("Day4/input.txt", "r") as my_file:
    lines = my_file.readlines()
    card_dict = dict()
    for line in lines:
        line = line.strip()
        match = re.match(r'Card\s+(\d+)', line)
        card_num = int(match.group(1))
        if card_num not in card_dict:
            card_dict[card_num] = 1
        else:
            card_dict[card_num] += 1
        num_left = re.findall(r'\d+', line.split(":")[1].split('|')[0])
        num_right = re.findall(r'\d+', line.split(":")[1].split('|')[1])
        matches_count = len(set(num_left) & set(num_right))
        copies = card_dict.get(card_num, 0)
        for i in range(card_num + 1, card_num + 1 + matches_count):
            if i not in card_dict:
                card_dict[i] = copies
            else:
                card_dict[i] += copies
print(sum(card_dict.values()))