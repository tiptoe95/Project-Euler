#!/bin/python3


#


def get_sides(max_len):
    triangles = []
    for a in range(1, max_len // 3):
        for b in range(a, max_len // 2):
            for c in range(b, max_len // 2):
                if a + b + c != max_len:
                    continue
                if valid_triangle(a, b, c):
                    triangles.append((a, b, c))
    return triangles


def valid_triangle(a, b, c):
    if (a**2 + b**2) == c**2:
        return True
    return False


def main():
    solutions = dict()
    for p in range(1, 1000):
        key, val = p, len(get_sides(p)) 
        solutions.update({key: val})
        print(key, val)
    print(max(solutions.keys(), key=lambda x:solutions[x]))


def test():
    p = 120
    triangles = get_sides(p)
    print(triangles)


if __name__ == "__main__":
    #test()
    main()
