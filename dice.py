#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import random
import sys
from aas import aa, get_aas

def main():
#	dice_aas = get_aas('aas/dice.txt', 'aas/dice.yml')
	'''
	check 1st arg
	'''
	try:
		n = int(sys.argv[1])
	except ValueError:
		print("1st argument must be integer")
		return 1
	except IndexError:
		print("need 1 or 2 arguments")
		return 1
	except:
		print("unexpected error in processing 1st argument")
		return 1
	if n <= 0 or n > 10:
		print("1st argument must be in [1,10]")
		return 1

	'''
	init random with 2nd arg
	'''
	try:
		random.seed(a=int(sys.argv[2]))
	except:
		random.seed()

	'''
	main part
	'''
	for i in range(n):
		m = random.randint(1,6)
		if i > 0:
			print(" ", end="")
		print(m, end="")
	print("")

	return 0


if __name__ == '__main__':
	main()

