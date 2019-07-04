import random


class ReturnGenerator:
    """
    Infinitely generate from iterable without consecutive repetitions
    """
    def __init__(self, data):
        self.data = data
        self.n = len(data) - 1
        self.last = None

    def __iter__(self):
        return self

    def __next__(self):
        ind = None
        if self.n > 1:
            while not ind or ind == self.last:
                ind = random.randint(0, self.n)
        self.last = ind
        return self.data[ind]
