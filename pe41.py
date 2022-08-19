#!/bin/python3


from helpers import prime
import itertools


def sieve_eratosthenes(limit):
    prime_range = range(limit+1)
    primes = [True for i in prime_range]
    p = 2
    while (p*p <= limit):
        if primes[p] == True:
            for i in range(p*p, limit+1, p):
                primes[i] = False
        p += 1
    primes = [x for x in prime_range if primes[x]]
    return primes


def get_pandigitals():
    pandigitals = []
    for j in range(1, 10):
        digits = set(range(1, j))
        # a number is divisible by 3 if and only if its digit sum is also divisible by 3
        if sum(digits) % 3 == 0:
            continue
        digits = (str(x) for x in digits)
        pandigits = [''.join(digits) for digits in itertools.permutations(digits)]
        pandigitals.extend(int(x) for x in pandigits)
    return pandigitals


def main():
    print("getting pandigitals")
    pandigits = get_pandigitals()
    print("generating primes")
    primes = sieve_eratosthenes(max(pandigits))
    print("finding max match")
    for prime in primes[::-1]:
        if prime in pandigits:
            print(f"{prime} is a pandigital")
            return
    return


def test():
    x = sieve_eratosthenes(100)
    print(x[::-1])


if __name__ == "__main__":
    main()
