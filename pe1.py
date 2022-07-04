"""Multiples of 3 and 5"""


answer = 0
for num in range(1000):
    if not num % 3 or not num % 5:
        answer += num
print(answer)
