#!/bin/python3


#


num_set = set(x for x in "123456789")


def is_pandigital(number: str) -> bool:
    if isinstance(number, int):
        number = str(number)
    if len(number) != 9 or "0" in number:
        return False
    return set(x for x in number) == num_set


def pandigital_product(number: int) -> int:
    num_str = ""
    multiplier = 1
    while len(num_str) < 9:
        product = number * multiplier
        num_str += str(product)
        multiplier += 1
    if multiplier < 3:
        return "0"
    return num_str


def main():
    pandigital_products = []
    limit = 100_000
    n = 1
    while n < limit:
        print(f"testing {n:,}", end="\r", flush=True)
        pan_prod = pandigital_product(n)
        if is_pandigital(pan_prod):
            pandigital_products.append(pan_prod)
        n += 1
    print()
    print(max(pandigital_products))


def test():
    a = "192837465"
    a = 192837465
    x = is_pandigital(a)
    print(x)


if __name__ == "__main__":
    main()
