import sys

for i,line in enumerate(sys.stdin):
	
	for j in range(len(line)):
		if line[j] == '0':
			print("0(zero) in", (i+1, j+1))
#		elif line[j] == 'O':
#			print("O(alphabet o) in", (i+1, j+1))
