#!/bin/python3


#


def word_value(word):
    value = 0
    for letter in word.upper():
        value += ord(letter) - 64
    return value


def main():
    word_file_path = r"inputs/input42.txt"
    with open(word_file_path, 'r') as word_file:
        word_list = [x.lstrip('"').rstrip('"') for x in word_file.readline().split(',')]

    triangle_numbers = [n*(n+1)/2 for n in range(1, 50)]
    triangle_word = 0
    for word in word_list:
        if word_value(word) in triangle_numbers:
            triangle_word += 1
    print(triangle_word)
    return triangle_word


def test():
    return


if __name__ == "__main__":
    main()
