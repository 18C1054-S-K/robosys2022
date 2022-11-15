#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import yaml

class aa:
	def __init__(self, strs, elses=None):
		self.strs = strs
		self.elses = elses
		self.height = len(self.strs)
		self.width = 0
		for s in self.strs:
			if len(s) > self.width:
				self.width = len(s)


	def show(self):
		for s in self.strs:
			print(s)


def get_aas(aa_txt_path, cutter_yml_path):
#	try:
		aas = []
		lst = []
		with open(cutter_yml_path, 'r') as f:
			temp = yaml.safe_load(f)
			if type(temp) == dict:
				if 'up' in temp and 'down' in temp:
					lst.append(temp)
			elif type(temp) == list:
				for e in temp:
					if 'up' in e and 'down' in e:
						lst.append(e)
		strs = []
		with open(aa_txt_path, 'r') as f:
			strs.extend(f.readlines())
		for i in range(len(strs)):
			strs[i] = strs[i][: -1]
		for c in lst:
			if 'up' in c and 'down' in c and int(c['down']) - int(c['up']) >= 0:
				c_ = c.copy()
				del c_['up'], c_['down']
				aas.append(aa(strs[int(c['up'])-1 : int(c['down'])], elses=c_))
		return aas
#	except: return None

def show_aas_in_row(aas, str_between_aas=None):
	if not type(aas) == list:
		return 0
	if len(aas) == 0:
		return 0

	if str_between_aas == None or not type(str_between_aas) == str:
		delimiter = ""
	else:
		delimiter = str_between_aas

	strs = []
	w_sum = 0
	for i in range(len(aas)):
		if type(aas[i]) == aa:
			for j in range(len(strs), aas[i].height):
				strs.append("")
			for j,s in enumerate(aas[i].strs):	
				strs[j] += aas[i].strs[j]
			w_sum += aas[i].width
			if i < len(aas) - 1:
				for j in range(len(strs)):
					strs[j] += " " * (w_sum - len(strs[j]))
					strs[j] += delimiter
				w_sum += len(delimiter)
		else:
			if i == len(aas)-1 and not len(delimiter) == 0:
				for j in range(strs):
					strs[j] = strs[j][: -len(delimiter)]
	for s in strs:
		space_len = 0
		for i in reversed(range(len(s))):
			if s[i] == " ":
				space_len += 1
			else:
				break
		if space_len == 0:
			print(s)
		else:
			print(s[: - space_len])

	return 0
