
import re
# Part 1
# result = 0
# with open("input.txt", "r") as my_file:
#     lines = my_file.readlines()
#     for line in lines:
#         tmp = list(filter(lambda x: x.isdigit(), line.strip()))
        
#         if len(tmp) == 1:
#             result += int(tmp[0] + tmp[0])
#         elif len(tmp) >= 2:
#              result += int(tmp[0] + tmp[-1])
        
# print(result)

#Part 2
number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
search_pattern = ('one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9')
result = 0
with open("Day1/part2test.txt", "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        line = line.strip()
        wordStart = ''
        wordEnd = ''
        foundStart = False
        foundEnd = False
        while len(line) > 0 and (not foundStart or not foundEnd):
            for word in search_pattern:
                if(not foundStart and line.startswith(word)):
                    wordStart = word
                    foundStart = True
                if(not foundEnd and line.endswith(word)):
                    wordEnd = word
                    foundEnd = True
                if(foundStart and foundEnd):
                    tmp0 = wordStart if number_dict.get(wordStart, None) == None else number_dict.get(wordStart)
                    tmp1 = wordEnd if number_dict.get(wordEnd, None) == None else number_dict.get(wordEnd)
                    res = int(tmp0 + tmp1)
                    result += res
                    break
            if not foundStart:
                line = line[1:]
            if not foundEnd:
                line = line[:-1]
print(result)                

        # nums = re.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', line.strip())
        # if nums:
        #     print(nums)
            # tmp0 = nums[0] if number_dict.get(nums[0], None) == None else number_dict.get(nums[0])
            # tmp1 = nums[-1] if number_dict.get(nums[-1], None) == None else number_dict.get(nums[-1])
            # result +=  int(tmp0 + tmp1)
        
