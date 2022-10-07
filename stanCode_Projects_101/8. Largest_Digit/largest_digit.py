"""
File: largest_digit.py
Name: Chunya Tsai
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integer
	:return: the largest number of each digit in n
	"""
	if n < 0:											# transfer negative number to positive
		n *= -1
	return find_largest_digit_helper(n, 1, 0)


def find_largest_digit_helper(n, level, largest):
	if n // level < 1:
		return largest
	else:
		last = (n // level) - (n // (level*10)) * 10		# the number of the last checked digit
		if largest < last:
			largest = last
		return find_largest_digit_helper(n, level*10, largest)


if __name__ == '__main__':
	main()
