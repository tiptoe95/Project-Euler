"""Sum square difference"""


def sum_square_diff(topnum):
    sum_squared = sum(range(topnum + 1))**2
    square_summed = sum(n**2 for n in range(topnum + 1))
    diff = sum_squared - square_summed
    print(diff)


if __name__ == '__main__':
    sum_square_diff(100)
