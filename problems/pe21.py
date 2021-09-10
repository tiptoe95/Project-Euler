"""Amicable numbers"""

def divisors(num):
    return [x for x in range(1, num) if num % x == 0]


def sum_amicable(num):
    matches = set()
    for a in range(1, num):
        b = sum(divisors(a))
        if b <= a: continue
        if sum(divisors(b)) == a:
            print(f"match! {a} & {b}")
            matches.add(a)
            matches.add(b)
    return sum(matches)


if __name__ == '__main__':
    print(sum_amicable(10000))