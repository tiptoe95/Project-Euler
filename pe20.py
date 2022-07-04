"""
Find the sum of the digits in the number 100!
"""

def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


def sum_fac_digits(num):
    digits = list(str(fac(num)))
    digits = map(int, digits)
    return sum(digits)

if __name__ == '__main__':
    print(sum_fac_digits(100))