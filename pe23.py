"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

1) initialize array of natural number up to 28123
2) fill array of all abundant numbers up to 28123
3) get sum of all combinations of abundant numbers not exceeding 28123 and zero the correxponding value in the natural number array
4) sum the remaining natural numbers