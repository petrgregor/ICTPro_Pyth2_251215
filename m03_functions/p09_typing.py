from typing import Optional


def add(x, y):
    result: int = x+y
    return result


print(add(5, 6))
print(add(3.7, 2))

number: int = 5
print(number)
# number="five"
number = 4
print(f"number = {number}")  # comment

# numbers:list[int] = []
numbers = [5]
#numbers.append(5)
print(numbers)
# numbers.append('q')

numbers2: list[int] = [2]
print(numbers2)

# optional_type:Optional[dict]


def find_user(user_id) -> Optional[dict]:
    if user_id > 1000:
        return None
    return {"id": user_id}


print(find_user(500))
print(find_user(5000))
