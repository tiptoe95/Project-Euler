#!/usr/bin/python3


def reciprocal_cycles():
    from decimal import Decimal

    max_len = 1
    for x in range(1, 100):
        ans = str(Decimal(1/x)).lstrip('0.')
        print(f"{x}: {ans}")

        if len(ans) < max_len:
            continue
        patterns = check_for_patterns(ans)
        print(f"\t{patterns}")
        if patterns:
            print(f"\tmax:{max(patterns, key=len)}")


def check_for_patterns(seq):
    pass


def is_pattern(subseq):
    pass


def cheater():
    num = longest = 1
    for n in range(3, 1000, 2):
        if n % 5 == 0:
            continue
        p = 1
        while (10**p) % n != 1:
            p += 1
        if p > longest:
            num, longest = n, p

    print(num)

if __name__ == '__main__':
    cheater()
    #reciprocal_cycles()
