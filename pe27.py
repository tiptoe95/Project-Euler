#!/usr/bin/python3


import threading
from helpers import prime


def main():
    # tuple of best parameters: (consecutive primes, a, b)
    max_primes = (0, 0, 0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes = test_quad(a, b)
            if primes > max_primes[0]:
                max_primes = (primes, a, b)
    streak, a, b = max_primes
    print(f"consecutive primes: {streak}")
    print(f"equation: n^2 + {a}n + {b}")
    print(f"a*b = {a*b}")


def test_quad(a, b):
    n = 0
    while n < 1000:
        num = n**2 + a*n + b
        if prime.isprime(num) == 0:
            return n
        else:
            n += 1
    print("error: n maxed out")
    return -1


if __name__ == "__main__":
    main()
