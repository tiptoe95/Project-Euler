#!/bin/python3


import itertools


def get_dividends(digits: str):
    return [int(str(digits)[i:i+3]) for i in range(1,8)]


def is_divisible(digits: str):
    quotients = [2, 3, 5, 7, 11, 13, 17]
    dividends = get_dividends(digits)
    truth_arr = [dividends[i] % quotients[i] == 0 for i in range(7)]
    return all(truth_arr)
    


def main():
    digit_seq = (str(x) for x in range(10))
    pandigitals = {''.join(digits) for digits in itertools.permutations(digit_seq)}

    matches = []
    for seq in pandigitals:
        if is_divisible(seq):
            matches.append(int(seq))
    print(sum(matches))

    return


def test():
    _ = is_divisible("1406357289")
    print(_)


if __name__ == "__main__":
    main()
