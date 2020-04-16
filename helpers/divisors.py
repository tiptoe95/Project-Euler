def get_divisors(num):
    if num < 1:
        if num == 0:
            return [0]
        raise ValueError("Negative numbers not allowed")

    divisors = set()
    for n in range(1, int(num**0.5) + 2):
        if num % n == 0:
            divisors.update({n, num//n})
    return sorted(list(divisors))


if __name__ == '__main__':
    import unittest

    tests = {
        1: 0,
        2: 1,
        3: 10,
        4: 100,
        5: -10,
    }
    for num, value in tests.items():
        result = get_divisors(value)
        print(f"{value} --> {result}")