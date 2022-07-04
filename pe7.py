"""10001st prime"""


def next_prime(primes):
    num = max(primes) + 2
    while True:
        for prime in primes:
            if num % prime == 0:
                num += 2
                break
        else:
            return num


def get_prime(goal):
    primes = {2, 3}
    while len(primes) < goal:
        prime = next_prime(primes)
        primes.add(prime)
        print(f"{len(primes)}: {max(primes)}")


if __name__ == '__main__':
    get_prime(10001)
