#!/usr/bin/python3


import os


def main(limit: int) -> int:
    print("generating primes...")
    primes = sieve_eratosthenes(limit)

    prime_list = []

    for prime in primes:
        print(f"running prime {prime} of {limit}...", end='', flush=True)
        match, combo = check_prime(prime, primes)
        if match:
            prime_list.append((prime, len(combo)))
        print("\r\x1b[K", end='', flush=True)

    prime = max(prime_list, key=lambda x: x[1])

    return prime


def sieve_eratosthenes(limit: int) -> list:
    sieve = [True for x in range(limit+1)]
    n = 2
    while (n**2 <= limit):
        if (sieve[n] == True):
            for i in range(n**2, limit+1, n):
                sieve[i] = False
        n += 1
    primes = [i for i, x in enumerate(sieve) if x]
    primes = [x for x in primes if x >= 2]
    return primes


def check_prime(prime: int, primes: list) -> bool:
    for start_idx in range(len(primes) - 1):
        for stop_idx in range(start_idx + 1, len(primes)):

            combo = primes[start_idx: stop_idx]
            prime_sum = sum(combo)

            if prime_sum > prime:
                continue

            if prime_sum == prime:
                return (True, combo)

    return (False, [])
            

def test():
    x = sieve_eratosthenes(50)
    print(x)


if __name__ == "__main__":
    prime_list = main(1_000_000)
    print(prime_list)
