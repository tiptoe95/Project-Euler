"""Highly divisible triangular number"""


def main(goal):
    triangle = 1
    a = 1
    count = 0
    while count <= goal:
        count = 0
        a += 1
        triangle += a
        ttx = triangle**0.5
        for i in range(1, ttx+1):
            if triangle % i == 0:
                count += 2
        if triangle == ttx*ttx:
            count -= 1                      # Correction for perfect square
    return triangle


def main2(goal) -> int:
    from ..helpers import prime

    for i in range(1, int(1e9)):
        n = i * (i+1) / 2
        if prime.num_facotrs(n) > goal:
            return n


if __name__ == '__main__':
    print(main2(500))
