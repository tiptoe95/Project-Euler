#!/bin/python3


import math
import time


def progress_bar(amt, total, runtime):
    percent = int((amt / total) * 100)
    full = '#' * ((percent // 5) + 1)
    empty = '-' * (19 - len(full))
    print("\033[2K\r", end='', flush=True)
    print(f"{full}{empty} [ {amt:,} of {total:,.0f} | {runtime} s ]", \
            end='', flush=True)


def sum_digit_factorials(number):
    return sum(math.factorial(int(x)) for x in str(number))


def main():

    n = 3
    limit = 3e6     # result for input of 9,999,999 is less than 3 million
    t_0 = time.time()
    matches = []

    while n < limit:
        if n % 10 == 0:
            t_n = time.time()
            runtime = t_n - t_0
            progress_bar(n, limit, int(runtime))
        fac_val = sum(math.factorial(int(x)) for x in str(n))
        if fac_val == n:
            matches.append(n)
        n += 1

    print('\n', matches)
    print(f"sum of matches: {sum(matches)}")
    return matches


def test():
    test_arr = [145, 40585, 9999999]
    for number in test_arr:
        ans = sum_digit_factorials(number)
        print(f"{number:,} : {ans:,}")


if __name__ == "__main__":
    main()
