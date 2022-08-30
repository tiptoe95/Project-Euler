#!/bin/python3


"""A collection of functions to support scripts involving prime numbers"""


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
prime_dict = dict.fromkeys(prime_list, 1)
lastn = prime_list[-1]


def _sieve_eratosthenes(num):
    """generate primes up to n"""
    sieve = [True for n in range(num+1)]
    p = 2
    while (p**2 <= num):
        if sieve[p]:
            for i in range(p**2, num+1, p):
                sieve[i] = False
        p += 1
    return [x for x in range(num+1) if sieve[x]]

def primes(limit):
    return _sieve_eratosthenes(limit)


def _isprime(n):
    """Raw check to see if n is prime. Assumes that prime_list is already populated"""
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n:                   # ... up to sqrt(n)
            break
        if not n % prime:
            isprime = 0
            break
    if isprime:
        prime_dict[n] = 1                       # Maintain a dictionary for fast lookup
    return isprime


def _refresh(x):
    """Refreshes primes up to x"""
    global lastn
    while lastn <= x:                           # Keep working until we've got up to x
        lastn += 1                              # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access


def prime(x):
    """Returns the xth prime"""
    global lastn
    while len(prime_list) <= x:                 # Keep working until we've got the xth prime
        lastn += 1                              # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access
    return prime_list[x]


def isprime(x):
    """Returns 1 if x is prime, 0 if not. Uses a pre-computed dictionary"""
    _refresh(x)                                 # Compute primes up to x (which is a bit wasteful)
    return prime_dict.get(x, 0)                 # Check if x is in the list


def factors(n):
    """Returns prime factors of n as a list"""
    _refresh(n)
    x, xp, f = 0, prime_list[0], []
    while xp <= n:
        if not n % xp:
            f.append(xp)
            n /= xp
        else:
            x += 1
            xp = prime_list[x]
    return f


def all_factors(n):
    """Returns all factors of n, including 1 and n"""
    f = factors(n)
    elts = sorted(set(f))
    numelts = len(elts)
    def gen_inner(i):
        if i > numelts:
            yield 1
            return
        thiselt = elts[i]
        thismax = f.count(thiselt)
        powers = [1]
        for j in range(thismax):
            powers.append(powers[-1] * thiselt)
        for d in gen_inner(i+1):
            for prime_power in powers:
                yield prime_power * d
    for d in gen_inner(0):
        yield d


def num_facotrs(n):
    """Returns the number of factors of n, including 1 and n"""
    div = 1
    x = 0
    while n > 1:
        c = 1
        while not n % prime(x):
            c += 1
            n /= prime(x)
        x += 1
        div *= c
    return div


def test():
    arr = _sieve_eratosthenes(100)
    print(arr)
    return


if __name__ == "__main__":
    test()


"""
Optimization notes:
Function access FAIRLY slower than Array access is SLIGHTLY slower than local variable access
Generators are SLIGHTLY slower than returning a list
Dictionary acces takes ZERO time
"""
