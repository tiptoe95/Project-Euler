"""Even Fibonacci numbers"""


seq = [0, 1]
while seq[-1] <= 4 * 10**6:
    seq.append(seq[-1] + seq[-2])
print(sum(x for x in seq if not x % 2))
