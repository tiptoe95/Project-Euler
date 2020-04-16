"""Largest prime factor"""


import math

factorand = 600851475143
primes = set()

factor = 2
while factor < math.sqrt(factorand):
    if not factorand % factor:
        print(f"{factorand} is divisible by {factor}")
        primes.add(factor)
        factorand = int(factorand / factor)
    if factor == 2:
        factor += 1
    else:
        factor += 2
else:
    primes.add(factorand)
print(sorted(list(primes), reverse=True))
