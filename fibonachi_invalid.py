"""Module that contains iterable FibonachiNumbers class"""

import itertools

class FibonachiNumbers:
    """This class is about Fibonachi"""
    class FibonachiNumbers_iter:
        """Auxiliary function to create list of fib numbers"""
        def __init__(self):
            self.current_1, self.current_2, self.current_3 = 1,1,1
        def __next__(self):
            """Auxiliary function to create list of fib numbers"""
            if self.current_1 < 0 or self.current_2 < 0 or self.current_3 < 0:
                raise StopIteration()
            self.current_3 = self.current_1
            self.current_1, self.current_2 = self.current_2, self.current_1 + self.current_2
            return self.current_3

    def __iter__(self):
        return FibonachiNumbers.FibonachiNumbers_iter()

f6f = FibonachiNumbers()
print (list(itertools.islice(f6f,10)))
for i, f in zip(itertools.count(1),
    itertools.islice(f6f, 10)):
    print(f"{i}){f}")
