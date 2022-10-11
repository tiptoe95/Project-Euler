#!/usr/bin/python3


from time import sleep


def main():
    max_sum = 1
    for a in range(100):
        for b in range(100):
            n = pow(a, b)
            digit_sum = sum(int(x) for x in str(n))
            max_sum = max(digit_sum, max_sum)
        print(f"testing {a} of 100", end="\r", flush=True)
        sleep(0.2)
    print()
    print(max_sum)


def test():
    return


if __name__ == "__main__":
    main()
