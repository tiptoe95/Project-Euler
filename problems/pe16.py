"""Power digit sum"""

def main(base, exp):
	num = base**exp
	digit_sum = sum(int(char) for char in str(num))
	print(digit_sum)
	return digit_sum

if __name__ == '__main__':
	main(2, 10**3)
