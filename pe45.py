#!/bin/python3


#


def triangle_gen():
    n = 1
    while True:
        num = n*(n+1)//2
        yield num
        n += 1


def pentagon_gen():
    n = 1
    while True:
        num = n*(3*n-1)//2
        yield num
        n += 1


def is_pentagon(num):
    x = ((24*num + 1)**0.5 + 1) / 2
    return x % 1 == 0


def hexagon_gen():
    n = 1
    while True:
        num = n*(2*n-1)
        yield num
        n += 1


def main():
    n = 1
    hex = hexagon_gen()
    for n in hex:
        print(f"{n:,}", end='\r', flush=True)

        if is_pentagon(n):
            print()
            print(n)


def test():
    t = triangle_gen()
    p = pentagon_gen()
    h = hexagon_gen()
    a, b, c = [], [], []
    for i in range(5):
        a.append(next(t))
        b.append(next(p))
        c.append(next(h))
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()
