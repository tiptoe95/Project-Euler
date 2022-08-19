#!/bin/python3


from helpers.prime import isprime


def is_truncable(num):
    num = str(num)
    nums = []
    for i in range(len(num)):
        nums.append(num[:len(num)-i])
        nums.append(num[i:len(num)])
    nums = [int(num) for num in nums]
    print(nums)
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
    if is_truncable(3797):
        print("tiggle")
    print("not tiggle")


if __name__ == "__main__":
    main()
