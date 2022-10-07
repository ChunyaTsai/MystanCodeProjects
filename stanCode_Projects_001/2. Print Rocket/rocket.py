"""
File: rocket.py
Name: Chunya Tsai
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3  # size of rocket, int, SIZE > 0


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	印出火箭頭
	"""
	for i in range(SIZE):
		for j in range(SIZE, i, -1):
			print(" ", end="")
		for j in range(i+1):
			print("/", end="")
		for j in range(i+1):
			print("\\", end="")
		print("")


def belt():
	"""
	印出聯結
	"""
	print("+", end="")
	for i in range(SIZE*2):
		print("=", end="")
	print("+")


def upper():
	"""
	印出火箭上半身
	"""
	for i in range(SIZE):
		print("|", end="")
		for j in range(SIZE-1, i, -1):
			print(".", end="")
		for j in range(i+1):
			print("/\\", end="")
		for j in range(SIZE-1, i, -1):
			print(".", end="")
		print("|")


def lower():
	"""
	印出火箭下半身
	"""
	for i in range(SIZE):
		print("|", end="")
		for j in range(i):
			print(".", end="")
		for j in range(SIZE, i, -1):
			print("\\/", end="")
		for j in range(i):
			print(".", end="")
		print("|")



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()