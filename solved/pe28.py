#!/bin/python3


#


def main():
    sum_nums = [1]
    
    #range to 1002 because 1001 is non-inclusive
    for n in range(3, 1002, 2):
        jump = n-1
        for i in range(4):
            sum_nums.append(n**2 - i*jump)

    print(sum(sum_nums))


if __name__ == "__main__":
    main()
