"""
File: boggle.py
Name: Chunya Tsai
----------------------------------------
User inputs a 4x4 matrix with any of alphabet.
This program will find all characters (with length >=4)
consist of the neighboring alphabet in inputted matrix.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Let user input 16 alphabets (4X4).
	Then, print out all characters (with length >=4) found in dictionary.txt
	consist of the neighboring alphabet from input.
	"""
	ans_lst = []					# all answers
	input_d = []					# user input
	for i in range(4):
		print(i+1, end='')
		s = str(input(' row of letters: '))

		if check_input(s):
			input_d.append(check_input(s))
		else:
			print("Illegal input!")
			break

	start = time.time()
	####################

	if len(input_d) == 4:
		d = read_dictionary()
		for x in range(4):
			for y in range(4):
				input_d[x][y][1] = False
				find_ans(x, y, input_d[x][y][0], input_d, d[input_d[x][y][0]], ans_lst)
				input_d[x][y][1] = True
		print(f'There are {len(ans_lst)} word(s) in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_ans(x, y, current_s, input_d, d, ans_lst):
	"""
	:param x: (int) x-coordinate of the current ch
	:param y: (int) y-coordinate of the current ch
	:param current_s: (itr) current string
	:param input_d: (list) user input
	:param d: (dict) simplified dictionary
	:param ans_lst:	(list) all answer
	:return:
	"""
	if len(current_s) >= 4:
		if current_s in d and current_s not in ans_lst:
			ans_lst.append(current_s)
			print('Found: "' + current_s + '"')

	for i in range(-1, 2):
		for j in range(-1, 2):
			cur_x = x + i
			cur_y = y + j

			# choose
			if 4 > cur_x >= 0 and 4 > cur_y >= 0 and input_d[cur_x][cur_y][1] is True:
				current_s += input_d[cur_x][cur_y][0]
				input_d[cur_x][cur_y][1] = False				# avoid duplicated character checking

				# explore
				if has_prefix(current_s, d):
					find_ans(cur_x, cur_y, current_s, input_d, d, ans_lst)

				# un-choose
				current_s = current_s[:-1]
				input_d[cur_x][cur_y][1] = True


def check_input(s):
	"""
	:param s: (str) user input
	:return: (list) Transfer s to a list. For illegal input, return an empty list.
	"""
	lst = []
	if len(s) == 7:
		for i in range(7):
			if i % 2 != 0:
				if s[i] != ' ':
					return []
			else:
				if s[i].isalpha():
					lst.append([s[i].lower(), True])
					# The boolean in above list is for next step. To avoid to check the duplicated character.
				else:
					return []
	return lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list.
	:return: (dict) key = letter a-z, value = all characters starts from key,
	only includes those characters in length >= 4
	"""
	simplify_d = {}
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:
				if line.strip()[0] not in simplify_d:
					simplify_d[line.strip()[0]] = [line.strip()]
				else:
					simplify_d[line.strip()[0]].append(line.strip())
	return simplify_d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param d: (list) simplified dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
