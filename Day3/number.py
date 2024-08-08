class Number:
    def __init__(self, x_start, x_end, y, num):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.num = num
    
    from symbol import Symbol
    def has_adjacent_symbol(self, symbols: list[Symbol]) -> bool:
        for symbol in symbols:
            x = symbol.x
            y = symbol.y
            
            if self.check(x - 1, y - 1):
                return True
            elif self.check(x, y - 1):
                return True
            elif self.check(x + 1, y - 1):
                return True
            elif self.check(x - 1, y):
                return True
            elif self.check(x + 1, y):
                return True
            elif self.check(x - 1, y + 1):
                return True
            elif self.check(x, y + 1):
                return True
            elif self.check(x + 1, y + 1):
                return True
        return False

            
        return True
    
    def check(self, x, y) -> bool:
        if y == self.y and \
            x >= self.x_start and \
            x <= self.x_end:
            return True
        return False


