""" Task: Fibonacci iterator
Vytvořte iterátor, který bude iterovat
prvky Fibonacciho posloupnosti.
"""


class FibIterator:

    def __init__(self, max_n=0):
        self.max_n = max_n

    def __iter__(self):
        self.n = 0
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.n < self.max_n:
            if self.n == 0:
                self.n += 1
                return self.a
            if self.n == 1:
                self.n += 1
                return self.b
            self.a, self.b = self.b, self.a+self.b
            self.n += 1
            return self.b
        raise StopIteration


# Create an object
fibonacci_iterator = FibIterator(2000000)

# Create an iterable from the object
fib_iterator = iter(fibonacci_iterator)

for i in fib_iterator:
    print(i)
    if i > 10:
        break
