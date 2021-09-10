"""Smallest multiple"""


import math


def smallest_multiple(factorand=1, top_num=20):
    limit = math.factorial(top_num)
    print(f"{top_num}! = {limit}")
    while factorand < limit:
        for factor in range(1, top_num+1):
            if not factorand % factor:
                continue
            factorand += 1
            break
        else:
            return factorand


if __name__ == '__main__':
    print(smallest_multiple())
    # todo: remove redundant factors from loop, multiply factors for answer
