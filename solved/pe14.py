"""Longest Collatz sequence"""


def main():
	len_dict = {}
	for num in range(1, 10**6 + 1):
		len_dict[str(num)] = run_seq(num)
		print(f"start: {num}\n\tlength: {len_dict[str(num)]}")
	ans = max(len_dict, key=len_dict.get)
	print(f"value of longest chain: {ans}")
	return 


def run_seq(start_num):
	num = start_num
	seq_len = 0
	while num > 1:
		seq_len += 1
		if num%2 == 0:
			num /= 2
		else:
			num = 3*num + 1
	else:
		return seq_len


if __name__ == '__main__':
	main()