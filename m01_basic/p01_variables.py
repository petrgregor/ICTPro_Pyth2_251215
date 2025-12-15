num1 = 10
num2 = num1

print(f"id(num1) = {id(num1)}, id(num2) = {id(num2)}")

num1 = 20
print(f"id(num1) = {id(num1)}, id(num2) = {id(num2)}")
print(f"num1 = {num1}, num2 = {num2}")

print("-"*80)

list1 = [1, 2, 3]
list2 = list1
print(f"id(list1) = {id(list1)}, id(list2) = {id(list2)}")
print(f"list1 = {list1}, list2 = {list2}")
list1.append(4)
print(f"id(list1) = {id(list1)}, id(list2) = {id(list2)}")
print(f"list1 = {list1}, list2 = {list2}")

print("-"*80)
number: int = 45
print(f"number = {number}")
number = 12.7
print(f"number = {number}")
number = "deset"
print(f"number = {number}")

print("-"*80)
a = 10
b = 20
print(f"a + b = {a + b}")

a = "first"
b = "second"
print(f"a + b = {a + b}")

print(f"type(a) = {type(a)}")

a = 1
b = 2
if isinstance(a, int) and isinstance(b, int):
    print(f"a + b = {a + b}")
else:
    raise ValueError("Expected int, but got str.")

print("-"*80)
for i in range(-1, -4, -1):
    print(i)

print(f"range(100000) = {range(100000)}")

print("-"*80)

fruits = ["apple", "banana", "lemon"]
print(f"fruits = {fruits}")
for fruit in fruits:
    print(fruit)
print("-"*40)
for i in range(len(fruits)):
    print(fruits[i])
print("-"*40)
for i, fruit in enumerate(fruits):
    print(f"Fruit '{fruit}' is at index {i}")
