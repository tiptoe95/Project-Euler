#!/bin/python3


import itertools


def get_permutations(top_digit=9):
    perms = [x for x in itertools.permutations(range(1, top_digit+1))]
    return perms


def flatten_digits(digit_list):
    number = int(''.join(str(x) for x in digit_list))
    return number


def test_equation(triplet):
    a, b, c = triplet
    return a * b == c


def generate_factors(digits):
    range_limit = len(digits) - 1
    equations = []
    for multiplicand_len in range(1, range_limit):
        for multiplier_len in range(1, range_limit):
            for product_len in range(1, range_limit):
                if multiplicand_len + multiplier_len + product_len != len(digits):
                    continue
                multiplicand_slice = digits[:multiplicand_len]
                multiplier_slice = digits[multiplicand_len:(range_limit-product_len+1)] 
                product_slice = digits[-product_len:]
                
                multiplicand = flatten_digits(multiplicand_slice)
                multiplier = flatten_digits(multiplier_slice)
                product = flatten_digits(product_slice)
                equations.append((multiplicand, multiplier, product))
    return equations


def test():
    digits = (1, 2, 3, 4, 5)
    x = generate_factors(digits)
    print(x)


def main():
    perms = get_permutations()
    matches = set()

    count = 0
    total = len(perms)
    for perm in perms:
        count += 1
        print(f"testing {count:,} of {total:,}", end='\r', flush=True)
        for equation in generate_factors(perm):
            if test_equation(equation):
                matches.add(equation[2])
    print()
    print(sum(matches))
    return sum(matches)


if __name__ == "__main__":
    main()
