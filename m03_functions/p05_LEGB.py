pi = 3.14

def outer():
    pi = 3.1415

    def inner():
        #nonlocal pi
        pi = 3.14159
        print(f"Inner: {pi} (Local)")

    inner()
    print(f"Outer: pi = {pi} (Enclosing)")


outer()
print(f"Global: pi = {pi} (Global)")

from math import pi
print(f"Built-in: pi = {pi} (Built-in)")