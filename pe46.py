#!/bin/python3


from helpers.prime import primes


prime_list = primes(1_000_000)


def test_composite(num):
    for prime in [x for x in prime_list if x < num]:
        for square in [x**2 for x in range(1, int(num**0.5) + 1)]:
            if prime + 2*square == num:
                return True
    return False


def main():
    i = 1
    while True:
        for j in range(1, i+1):
            composite = (2*i + 1) * (2*j + 1)
            if not test_composite(composite):
                print(composite)
                return
        i += 1


def test():
    return


if __name__ == "__main__":
    main()
