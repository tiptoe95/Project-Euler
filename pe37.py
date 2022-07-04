#!/bin/python3


from .. import helpers.prime.isprime 


def is_truncable(num):
    num = str(num)
    revnum = num[::-1]
    nums = []
    for i in range(len(num)):
        nums.append(num[:len(num)-i])
        nums.append(revnum[:len(num)-i])
    for j in nums:
        if not isprime(j):
            return False
    return True


def main():
    matches = []
    n = 9
    while len(matches) < 11:
        if is_truncable(n):
            matches.append(n)
        n += 1
    ans = sum(matches)
    print(ans)
    return ans


def test():
    is_truncable(12345)


if __name__ == "__main__":
    test()
