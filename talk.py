#!/usr/bin/env python3

def talk():
	i = input('continue?(y/n): ')
	if i == 'y':
		return 0
	elif i == 'n':
		print('bye')
		return 1
	else:
		print('invalid input')
		return 0


def main():
	r = 0
	while r == 0:
		r = talk()


if __name__ == '__main__':
	main()
