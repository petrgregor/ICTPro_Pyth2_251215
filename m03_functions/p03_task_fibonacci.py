""" Task 3
Napište funkci, která vrátí n-tý prvek Fibonacciho posloupnosti.
https://cs.wikipedia.org/wiki/Fibonacciho_posloupnost
0, 1, 1, 2, 3, 5, 8, 13, 21,...
fib(0) = 0
fib(5) = 5
fib(6) = 8
fib(n) = fib(n-1) + fib(n-2)
"""

# pomocí rekurze -> NEEFEKTIVNÍ
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    num1 = 0
    num2 = 1
    #suma = 0
    for i in range(2, n+1):
        """suma = num1 + num2
        num1 = num2
        num2 = suma"""
        num1, num2 = num2, num1+num2
    return num2


def fib1000() -> int:
    i = 1
    while len(str(fib(i))) < 1000:
        i += 1
    return i


if __name__ == "__main__":
    #for i in range(120):
    #    print(f"fib({i}) = {fib(i)}")

    print("="*80)
    f1000 = fib1000()
    print(f"fib({f1000}) = {fib(f1000)}")
