#!/bin/python3


#


def check_frac(test_num, test_denom, num, denom):
    num1 = int(test_num)
    denom1 = int(test_denom)
    if num1 >= denom1:
        return False
    try:
        if num1 / denom1 == num / denom:
            return True
        else:
            return False
    except ZeroDivisionError:
        return False


def get_fracs(num, denom):
    fracs = []
    test_num, test_denom = map(str, [num, denom])
    if test_num[0] == test_denom[0]:
        fracs.append((test_num[1], test_denom[1]))
    if test_num[0] == test_denom[1]:
        fracs.append((test_num[1], test_denom[0]))
    if test_num[1] == test_denom[0]:
        fracs.append((test_num[0], test_denom[1]))
    if test_num[1] == test_denom[1]:
        # skip trivial results, such as 70/60 -> 7/6
        fracs.append((test_num[0], test_denom[0]))
        if test_num[1] == "0":
            fracs.pop()
    for test_num, test_denom in fracs:
        if check_frac(test_num, test_denom, num, denom):
            return True
    return False



def main():
    res = []
    for j in range(10, 100):
        for k in range(10, 100):
            if j >= k:
                continue
            if get_fracs(j, k):
                res.append((j, k))
    print(res)


if __name__ == "__main__":
    main()
