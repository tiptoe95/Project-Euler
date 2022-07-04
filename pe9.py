"""Special Pythagorean triplet"""


import time


def main():
    c = 1
    while True:
        print(f"trying c={c}")
        for a in range(1, 1001):
            b = 1000 - (a + c)
            if a**2 + b**2 == c**2:
                print(f"a: {a}\nb: {b}\nc: {c}")
                return a*b*c
        c += 1


def main2(s):
    m = 2
    while True:
        n = 1
        while n < m:
            a = 2*m*n
            b = m**2 - n**2
            c = m**2 + n**2
            if a+b+c == s and 2*m*(m+n) == s:
                return a, b, c
            n += 1
        m += 1
        if m > s:
            return None


def time_func(fn, *args):
    start_time = time.time()
    res = fn(*args)
    delta_time = time.time() - start_time
    print(f"{delta_time} seconds for {fn}")
    return res


if __name__ == '__main__':
    t1 = time.time()
    a = main()
    print(f"main: {time.time() - t1}")

    t1 = time.time()
    a, b, c = main2(1000)
    print(f"a: {a}\nb: {b}\nc: {c}")
    print(f"main: {time.time() - t1}")
