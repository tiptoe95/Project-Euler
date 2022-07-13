#!/bin/python3


#


def get_digit(n):
    digit_str = ""
    i = 0
    while len(digit_str) < n:
        i += 1
        digit_str += str(i)
    return digit_str[n-1] 


def product(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0]*product(arr[1:])


def main():
    digits = [10**p for p in range(7)]
    ans = [int(get_digit(n)) for n in digits]
    res = product(ans)
    print(res)    


def test():
    print(get_digit(12))
    print(get_digit(3))
    print(get_digit(15))


if __name__ == "__main__":
    #test()
    main()
