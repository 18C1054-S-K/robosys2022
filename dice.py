#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import random
import sys
from aas import aa, get_aas, show_aas_in_row

def main():
	'''  check 1st arg  '''
	try:
		n = int(sys.argv[1])
	except ValueError:
		if sys.argv[1] == "-h":
			print("throw dices & calcurate sum of their roll")
			print("  1st argument: how many dices")
			print("  2nd argument: seed of random")
			print("")
			print("NOTE  * 1st arg must be in [1,10]")
			print("      * if 2nd arg is None or invalid, seed is current time")
		else:
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

	'''  init random with 2nd arg  '''
	try:
		random.seed(a=int(sys.argv[2]))
	except:
		random.seed()

	'''  read dice aa  '''
	dice_aas = get_aas('aas/dice.txt', 'aas/dice.yml')

	'''  main part  '''
	ms = [random.randint(1,6) for i in range(n)]
	for i in range(n // 5):
		show_aas_in_row([dice_aas[ms[j] - 1] for j in range(i*5, (i+1)*5)], str_between_aas="   ")
		if not i == n // 5 - 1:
			print("")
	show_aas_in_row([dice_aas[ms[i] - 1] for i in range(5*(n//5), n)], str_between_aas="   ")
	print("")
#	print(ms)
	print("sum:", sum(ms))

	return 0


if __name__ == '__main__':
	main()

