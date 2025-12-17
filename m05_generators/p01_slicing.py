
#           0    1    2    3    4    5    6    7    8
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#         0   1    2    3    4    5    6    7    8    9

print(f"letters[4] = {letters[4]}")
print(f"letters[-5] = {letters[-5]}")
print(f"letters[2:5] = {letters[2:5]}")
print(f"letters[4:5] = {letters[4:5]}")
print(f"letters[4:4] = {letters[4:4]}")

print(f"letters[:] = {letters[:]}")
print(f"letters[::-1] = {letters[::-1]}")
print(f"letters[::2] = {letters[::2]}")

letters.append('j')
print(f"letters = {letters}")

letters.insert(3, "Z")
print(f"letters = {letters}")

result = letters.remove("Z")
print(f"letters = {letters}")
print(result)

result = letters.pop()
print(f"letters = {letters}")
print(result)

letters_copy = letters[::-1]
print(f"letters_copy = {letters_copy}")
letters_copy.sort()
print(f"letters_copy = {letters_copy}")

print("="*80)
my_range = range(1000000)
print(f"my_range = {my_range}")
#next(my_range)
for i in my_range:
    print(i)
    if i > 5:
        break

print("-"*40)
for i in my_range:
    print(i)
    if i > 15:
        break

print(list(my_range[5:20]))
print(list(my_range)[5:20])
