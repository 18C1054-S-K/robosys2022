#!/usr/bin/env python3

import sys
from aas import aa, get_aas

def maini_():
	dice_aas = get_aas('aas/dice.txt', 'aas/dice.yml')
	for i in sys.stdin:
		try:
			dice_aas[int(i)-1].show()
		except: pass


def main():
	dice_aas = get_aas('aas/dice.txt', 'aas/dice.yml')
	r = 0
	while r == 0:
		i = input("input 1~6(quit to n): ")
		try:
			dice_aas[int(i)-1].show()
			r = 0
		except:
			if i == 'n':
				r = -1
			else:
				r = 0


if __name__ == '__main__':
	main()


