#!/bin/python3


#


def count(coin_values, m, goal):

    # table[i] stores the number of solutinos for value i
    table = [0 for k in range(goal+1)]

    # base case
    table[0] = 1

    # Pick all coins one by one and update table values
    for i in coin_values:
        for j in range(i, goal+1):
            table[j] += table[j-i]
    
    return table[goal]

            

# Returns the number of arrangements to form 'n'
def solve(n, coin_values, lookup = {}):
    
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1    # i.e. n is $1 and x is a 1-dollar coin ---> only 1 possible combo 

    # Memoization
    if n not in lookup:
        lookup[n] = sum(solve(n-x, coin_values) for x in coin_values)
        print(f"lookup[{n}]: \n{lookup[n]}")
    return lookup[n]


def main():
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
    goal = 200
    #solutions = solve(goal, coin_values)
    solutions = count(coin_values, len(coin_values), goal)
    print(f"Number of solutions: {solutions}")


if __name__ == "__main__":
    main()

