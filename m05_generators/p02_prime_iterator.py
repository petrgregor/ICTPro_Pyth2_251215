from m03_functions.p01_task_prime_numbers import is_prime


class PrimeIterator:

    def __init__(self, max_n=0):
        self.max_n = max_n

    def __iter__(self):
        self.n = 0
        self.last_prime = 1
        return self

    def __next__(self):
        if self.n < self.max_n:
            # najdeme další prvočíslo
            i = self.last_prime+1
            while True:
                if is_prime(i):
                    self.n += 1
                    self.last_prime = i
                    return i
                i += 1
        raise StopIteration


prime_iterator = PrimeIterator(3)
iterator = prime_iterator.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))
print(next(iterator))

print("-"*40)

for i in iterator:
    print(i)
