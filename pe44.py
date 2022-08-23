#!/bin/python3


#


def main():
    matches = []
    pentags = [int(n*(3*n-1)/2) for n in range(1, 10000)]
    print(pentags[-5:])
    for j in pentags:
        for k in pentags:
            p_sum = j+k
            diff = abs(j-k)
            if p_sum in pentags and diff in pentags:
                print(f"match with {j} and {k}")
                matches.append(diff)
    ans = min(matches)
    print(ans)
    return ans


def test():
    return


if __name__ == "__main__":
    main()
