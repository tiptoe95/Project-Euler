"""Summation of primes"""


def main():
    limit = 2e6
    primes = [2]
    num = 3
    while num < limit:
        for prime in primes:
            if num % prime == 0:
                break
            if prime > num**0.5:
                primes.append(num)
                break
        else:
            primes.append(num)
        num += 2
        print(max(primes))
    print(sum([prime for prime in primes if prime < limit]))


def main2(limit):
    sievebound = int((limit-1) / 2)     # Last index of sieve
    sieve = [False] * sievebound
    crosslimit = (int(limit**0.5) - 1) // 2
    for i in range(crosslimit):
        if not sieve[i]:
            for j in range (2*i*(i+1) - 1, sievebound, 2*i+1):
                sieve[j] = True
    sum = 2
    for i in range(sievebound):
        if not sieve[i]:
            sum += 2*i+1
    return sum


if __name__ == '__main__':
    x = main2(2e6)
    print(x)
