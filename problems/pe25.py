"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fib1000():
    fib = [1,1]
    while len(str(fib[-1])) < 1000:
        fib.append(sum(fib[-2:]))
    print("length: ", len(fib))
    print(len(str(fib[-1])))


if __name__ == '__main__':
    fib1000()
