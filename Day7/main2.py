
import re
from functools import reduce
import math

# Part 2

card_ranks = \
{
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def rle_encode(input: str):
    result = {}
    for c in input:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result

def validate_cards(input: dict) -> int:
    jokers_count = input.get('J', 0)
    input.pop('J', None)
    card_counts = [x for x in input.values()]
    if len(card_counts) == 0:
        return 7
    
    idx_max = max(enumerate(card_counts), key=lambda x: x[1])[0]
    card_counts[idx_max] += jokers_count
    if card_counts.count(5) == 1:
        return 7
    elif card_counts.count(4) == 1:
        return 6
    elif card_counts.count(3) == 1 and card_counts.count(2) == 1:
        return 5
    elif card_counts.count(3) == 1:
        return 4
    elif card_counts.count(2) == 2:
        return 3
    elif card_counts.count(2) == 1:
        return 2
    else:
        return 1

def determine_ranks(input: list, counter_ranks: int):
    ranks = []
    res = []
    for cards in input:
        tmp = [card_ranks[x] for x in cards[0]]
        z = (cards[0], cards[1], tmp)
        res.append(z)
    res.sort(key=lambda x: x[2])
    for r in res:
        c = r[0]
        b = r[1]
        b *= counter_ranks
        counter_ranks += 1
        ranks.append(b)
    return sum(ranks), counter_ranks




with open("Day7/input.txt", "r") as my_file:
    lines = [x.strip() for x in my_file.readlines() if x.strip() != '']
    ranks = {}
    for line in lines:
        g = re.search(r"^(\w+) (\d+)$", line)
        card = g.group(1)
        bid = int(g.group(2))
        tmp = rle_encode(card)
        rank = validate_cards(tmp)
        if rank not in ranks:
            ranks[rank] = [(card, bid)]
        else:
            tmp_list = ranks[rank]
            tmp_list.append((card, bid))
            ranks[rank] = tmp_list
    
    counter_ranks = 1
    results = []
    for i in sorted(ranks.keys()):
        cards = ranks[i]
        if len(cards) == 1:
            c = cards[0]
            b = c[1]
            b *= counter_ranks
            counter_ranks += 1
            results.append(b)
        else:
            s, counter_ranks = determine_ranks(cards, counter_ranks)
            results.append(s)
    result = sum(x for x in results)
    pass
