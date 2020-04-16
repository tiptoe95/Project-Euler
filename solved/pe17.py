"""Number letter counts"""

word_dict = {
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen",
	20:"twenty",
	30:"thirty",
	40:"forty",
	50:"fifty",
	80:"eighty"
	}


def get_letter_count(num):
	letter_count = 0	

	if num >= 1000:
		letter_count += len(word_dict[num//1000]) + len("thousand")
		if 0 < num%1000 < 100:
			letter_count += len("and")
		elif num%1000 == 0:
			return letter_count
		letter_count += get_letter_count(num%1000)

	elif num >= 100:
		letter_count += len(word_dict[num//100]) + len("hundred")
		if num % 100 > 0:
			letter_count += len("and")
		elif num % 100 == 0:
			return letter_count
		letter_count += get_letter_count(num%100)

	elif num >= 20:
		if num in word_dict:
			letter_count += len(word_dict[num])
		elif num-(num%10) in word_dict:
			letter_count += len(word_dict[num-(num%10)])
		else:
			letter_count += len(word_dict[num//10]) + len("ty")
		letter_count += get_letter_count(num%10)

	elif num >= 1:
		letter_count += len(word_dict[num])
	elif num == 0:
		pass
	else:
		raise ValueError(f"Invalid number: {num}")

	return letter_count


def get_word(num):
	word = ""
	digits = [int(digit) for digit in str(num)]

	if len(digits) == 4:
		if digits[0] == 0:
			word = get_word(digits[1:])
		word += word_dict[digits[0]] + " thousand"
		if digits[1:] == [0, 0, 0]:
			pass
		else:
			word += get_word(''.join(map(str, digits[1:])))

	elif len(digits) == 3:
		if digits[0] == 0:
			word += " and " + get_word(digits[1:])
		else:
			word = word_dict[digits[0]] + " hundred"
			if digits[1:] == [0, 0]:
				pass
			else:
				word += " and " + get_word(''.join(map(str, digits[1:])))

	elif len(digits) == 2:
		if digits[0] == 0:
			word += get_word(''.join(map(str, digits[1:])))
		else:
			num = int(f"{digits[0]}{digits[1]}")
			if num in word_dict:
				word += word_dict[num]
			elif digits[0] in {2, 3, 4, 5, 8}:
				word += word_dict[int(f"{digits[0]}0")]
				word += get_word(''.join(map(str, digits[1:])))
			else:
				word += word_dict[digits[0]] + "ty"
				word += get_word(''.join(map(str, digits[1:])))


	elif len(digits) == 1:
		if digits[0] == 0:
			pass
		else:
			word += word_dict[digits[0]]

	return word


def main(limit):
	total_letters = 0
	for num in range(1, limit+1):
		word = get_word(num)
		num_letters = get_letter_count(num)
		print(f"{num}: {word} -- {num_letters}")
		total_letters += num_letters
	return(total_letters)


if __name__ == '__main__':
	res = main(10**3)
	print(res)