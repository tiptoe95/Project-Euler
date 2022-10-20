#!/usr/bin/python3


from itertools import permutations


def main():
    cubes = generate_cubes(1_000_000)
    n = 1
    while (n := n + 1) > 0:
        print(f"checking {n:,}...", end='\r', flush=True)
        x = n**3
        if x in cubes:
            perms = get_perms(x)
            perm_count = 0
            for perm in perms:
                if perm in cubes:
                    perm_count += 1
                if perm_count > 5:
                    break
            if perm_count == 5:
                print()
                print(f"FOUND MATCH: {x}")
                return


def generate_cubes(limit):
    cubes = [x**3 for x in range(limit)]
    return cubes


def get_perms(number):
    """

    number: float - 
    
    return: list -
    """
    perms = permutations(list(str(number)))
    joined_perms = [int(''.join(x)) for x in perms]
    return joined_perms


def test():
    return


if __name__ == "__main__":
    main()
