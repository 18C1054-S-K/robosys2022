#!/usr/bin/env python3

import yaml

class aa:
	def __init__(self, strs, attrs=None):
		self.strs = strs
		self.attrs = []


	def show(self):
		for s in self.strs:
			print(s, end='')


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
		for c in lst:
			if 'up' in c and 'down' in c and int(c['down']) - int(c['up']) >= 0:
				aas.append(aa(strs[int(c['up'])-1 : int(c['down'])]))
				c_ = c.copy()
				del c_['up'], c_['down']
				aas[len(aas)-1].attrs = c_
		return aas
#	except: return None
