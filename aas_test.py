#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import sys
import yaml
from aas import aa, get_aas, show_aas_in_row

def main():
	test_aas = get_aas(r"aas/"+sys.argv[1]+r".txt", r"aas/"+sys.argv[1]+r".yml")
	for i,a in enumerate(test_aas):
		print(r"( No.", i+1, ")")
		a.show()
		print("width :", a.width)
		print("height:", a.height)
		d = {"else": a.elses.copy()}
		print(yaml.dump(d))

	show_aas_in_row(test_aas, str_between_aas="   ")


if __name__ == '__main__':
	main()
