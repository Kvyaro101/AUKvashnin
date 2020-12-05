"""Module that contains iterable FibonachiNumbers class"""

class FibonachiNumbers:
    """This class is about Fibonachi"""
    def __init__(self,number):
        self.number = number
        self.i = 0
        self.list = []
        self.current = 1
        self.current_list = []
    def fib_list(self):
        """Auxiliary function to create list of fib numbers"""
        while self.i < self.number:
            self.list.append(self.current)
            self.i += 1
            try:
                self.current = self.current + self.list[-2]
            except IndexError:
                pass
        return self.list

    def __iter__(self):
        """It creates and returnes iterator"""
        self.current_list = FibonachiNumbers.fib_list(self)
        return FibonachiNumbers(self.number).FibonachiIterator(self.number,self.current_list)

    class FibonachiIterator:
        """Inner iterator-class of FibonachiNumbers class"""
        def __init__(self,number,fib_list):
            self.number, self.fib_list, self.i = number, fib_list, 0
        def __next__(self):
            if self.i >= self.number:
                raise StopIteration()
            j = self.i
            self.i += 1
            return self.fib_list[j]
        def previous(self):
            """Shows previous member of Fibonachi numbers"""
            if self.i <= 0:
                raise StopIteration()
            j = self.i
            self.i -= 1
            return self.fib_list[j]

f6f = FibonachiNumbers(8)
f6fi = iter(f6f) # Во время леции не мог отделаться от ассоциации с Grumman F6F
while True:
    try:
        print(next(f6fi))
    except StopIteration:
        print("The End of Fibonachi Numbers")
        break
