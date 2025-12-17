from mypyc.primitives.misc_ops import yield_from_except_op


def simple_generator():
    yield 1
    yield 2
    yield "three"
    yield "four"
    yield 5

simple_gen = simple_generator()
print(next(simple_gen))
print(next(simple_gen))
print(next(simple_gen))
print(next(simple_gen))
print(next(simple_gen))
# print(next(simple_gen))  # StopIteration


def countdown(n):
    print(f"Starting countdown from {n}...")
    while n > 0:
        yield n
        n -= 1
    print(f"Countdown finished.")


print("="*80)
my_countdown = countdown(10)
my_count = my_countdown
print("-"*40)
for i in my_count:
    print(i)


def fibonacci_generator(max_n):
    a = 0
    b = 1
    yield a
    yield b
    for i in range(2, max_n+1):
        a, b = b, a+b
        yield b
    print("END")


for i in fibonacci_generator(20):
    print(i)


def my_generator(n):
    yield 2
    yield 3
    n_ = 3
    i = 3
    n_ += 2
    yield n_
    while i < n:
        i += 1
        n_ += 2
        yield n_
        n_ += 4
        yield n_

print("="*80)
for i in my_generator(50):
    print(i)

print("="*80)
my_gen = (x ** 2 for x in range(1000000))
print(f"my_gen = {my_gen}")
for i in my_gen:
    print(i)
    if i > 20:
        break
print(f"sum(my_gen) = {sum(my_gen)}")