"""
Výpočet faktroiálu.
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!
0! = 1
"""

def fact(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


if __name__ == "__main__":
    for i in range(200):
        print(f"{i}! = {fact(i)}")
