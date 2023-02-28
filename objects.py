class Investor:
    cash: int
    stock: int
    prob: float

    def __init__(self, cash, stock, prob):
        self.cash = cash
        self.stock = stock
        self.prob = prob

    def __str__(self):
        return f"This investor has ${self.cash} and {self.stock} stocks"