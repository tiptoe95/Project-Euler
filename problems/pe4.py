"""Largest palindrome product"""


palis = []
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        prod = str(num1*num2)
        if prod[::-1] == prod:
            palis.append(int(prod))
print(sorted(palis, reverse=True))
