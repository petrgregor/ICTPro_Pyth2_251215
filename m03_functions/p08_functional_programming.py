from m03_functions.p01_task_prime_numbers import is_prime
from m03_functions.p04_recursion import fact
from m03_functions.p07_function_factory import double, triple


def add(a: int, b: int) -> int:
    return a + b

add2 = lambda a, b: a + b

print(f"add2(5, 3) = {add2(5, 3)}")

print("filter()")
gt5 = lambda x: x > 5
print(f"gt5(9) = {gt5(9)}")

print("-"*80)
result = filter(gt5, [1, 2, 3, 8, 9, 2, 0, 7])
print(result)  # <filter object at 0x000002527A53C940>
print(list(result))  # [8, 9, 7]

print("-"*80)
numbers = [5, 20, 7, 9, 20, 7, 9, 9, 6, 1, 11, 101]
print(list(filter(lambda x: x % 2 == 0, numbers)))
print("-"*80)
print(list(filter(lambda x: is_prime(x), numbers)))
print(list(filter(is_prime, numbers)))

print("map")
#map(<function>, <collection>)
print(list(map(lambda x: x+1, [1, 5, 8, 9])))
print(list(map(lambda x: double(x), [1, 2, 3, 4, 5])))
double_list = list(map(lambda x: double(x), [1, 2, 3, 4, 5]))
double_list = list(map(double, [1, 2, 3, 4, 5]))
for number in double_list:
    print(number)

print(list(map(triple, [1, 2, 3, 4, 5, 6])))

print(list(map(str.upper, ['a', 'b', 'c'])))

my_list = [double(x) for x in numbers]
print(my_list)

my_list2 = []
for i in numbers: #range(0, 20, 2):
    my_list2.append(double(i))
print(my_list2)

print("-"*80)
numbers2 = [fact(x) for x in [-5, 0, 5, 6, 9, -3] if x >= 0]
print(numbers2)