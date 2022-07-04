#!/bin/python3


#


def sum_powers(subject, power):
    power_sum = sum(int(digit)**power for digit in str(subject))
    return int(power_sum)


if __name__ == "__main__":
    stop_limit = 1_000_000      # no 7 (or higher) digit number could possibly be a solution (at least for powers <6)
    matches = []
    power = 5
    n = 1
    while n < stop_limit:
        n += 1
        if sum_powers(n, power) == n:
            matches.append(n)
            print(n)
    print("all matches found")
    print(sum(matches))

