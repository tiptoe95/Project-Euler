#!/bin/python3


#


def check_palindrome(num):
    rev = num[::-1]
    if rev == num:
        return True
    return False


def main():
    limit = 1e6
    res = []
    n = 1
    while n < limit:
        print(f"{n}\r", end='', flush=True)
        binary = "{0:b}".format(n)
        if check_palindrome(binary) and check_palindrome(str(n)):
            res.append(n)
        n += 1
    ans = sum(res)
    print(len(res))
    print(ans)
    return ans


if __name__ == "__main__":
    main()
