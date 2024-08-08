class Symbol:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    def is_gear_symbol(self, numbers: list) -> list[int]:
        res = list()
        for num in numbers:
            if num.has_adjacent_symbol([self]):
                res.append(num)
        return res

