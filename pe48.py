#!/usr/bin/python3


#


def truncate(number, size):
    number = str(number)[-10:]
    return int(number)


def main():
    limit = 1000
    ans = 0
    for n in range(1, limit+1):
        ans += n**n
        ans = truncate(ans, 10)
        print(f"adding {n:,} of {limit:,}", end = "\r", flush=True)
    print()
    print(ans)


def test():
    limit = 20
    ans = 0
    for n in range(1, limit+1):
        ans += n**n
        ans = truncate(ans, 10)
        print(ans)
        


if __name__ == "__main__":
    main()
