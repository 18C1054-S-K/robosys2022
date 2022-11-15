#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import sys
import yaml
from aas import aa, get_aas, show_aas_in_row

def find_aa(aas_list, name):
	for a in aas_list:
		if a.elses["name"] == name:
			return a


def main():
	test_aas = get_aas(r"aas/robosys2022.txt", r"aas/robosys2022.yml")

	l = []
	l.append(find_aa(test_aas, "R"))
	l.append(find_aa(test_aas, "O"))
	l.append(find_aa(test_aas, "B"))
	l.append(find_aa(test_aas, "O"))
	l.append(find_aa(test_aas, "S"))
	l.append(find_aa(test_aas, "Y"))
	l.append(find_aa(test_aas, "S"))
	l.append(find_aa(test_aas, "year"))
	show_aas_in_row(l, str_between_aas="   ")


if __name__ == '__main__':
	main()
