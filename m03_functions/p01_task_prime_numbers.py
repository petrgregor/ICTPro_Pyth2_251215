""" Task 1
Napište funkci is_prime(), která má jediný argument (celé číslo) a vrací True, pokud je
zadané číslo prvočíslo, jinak False.
"""
from typing import List


#debug = True

def is_prime(n: int, debug: bool = False) -> bool:
    if not isinstance(n, int):
        raise TypeError("Argument must be integer.")
    if n < 1:
        raise ValueError("Number must be positive.")
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    iterations = 0
    for i in range(3, int(n ** (1/2))+1, 2):
        iterations += 1
        if n % i == 0:
            return False
    if debug:
        print(f"Number of iterations: {iterations}")
    return True


""" Task 2
Napište funkci primes_list(n), která vrací seznam prvočísel <= n.
"""
def primes_list(n: int) -> List[int]:
    if not isinstance(n, int):
        raise TypeError("Argument must be integer.")
    result = []
    if n >= 2:
        result = [2]
    for i in range(3, n+1, 2):
        if is_prime(i):
            result.append(i)
    return result


if __name__ == "__main__":
    #print(is_prime(7.2))  # TypeError: Argument must be integer.
    #print(is_prime(-5))  # ValueError: Number must be positive.
    for i in range(1, 30):
        print(f"Number {i}", end=" ")
        if is_prime(i):
            print(f"is prime.")
        else:
            print(f"is not prime.")
    print("-"*80)
    number = 103
    print(f"{number} is prime: {is_prime(number, True)}")

    print("-"*80)
    print(f"primes_list[{number}]: {primes_list(number)}")
