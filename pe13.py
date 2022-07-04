def sum_long(num_arr):
	num_str = str(sum(num_arr))
	print(num_str[:10])


if __name__ == '__main__':
	with open('inputs/input13.txt', 'r') as input_file:
		input = [int(line) for line in input_file]
	sum_long(input)