#!/bin/python3


import math


def build_primes(limit):
    prime_list = []
    for n in range(int(limit)):
        if is_prime(n):
            prime_list.append(n)
        print(f"Prime list: {n}", end='', flush=True)
        print("\033[K2\r", end='', flush=True)
    print("\n")
    return prime_list


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def check_rots(rot_tuple):
    for rot in rot_tuple:
        if not is_prime(rot):
            return False
    return True


def rotations(n):
    rots = []
    n = str(n)
    for j in range(len(n)):
        combo_string = 2 * n
        combo = combo_string[j:j+len(n)]
        rots.append(int(combo))
    return rots


def main():
    prime_list = build_primes(1e6)
    circular_primes = set()
    for number in prime_list:
        rots = rotations(number)
        if check_rots(rots):
            circular_primes.add(number)
    print(circular_primes)
    print(len(circular_primes))


def test():
    prime_test_list = [-1, 0, 1, 2, 7, 35, 2999401]
    for x in prime_test_list:
        print(f"is_prime({x}): {is_prime(x)}")
    rotation_check_list = [123, 4567, 2]
    for x in rotation_check_list:
        print(rotations(x))


if __name__ == "__main__":
    main()
    #test()
