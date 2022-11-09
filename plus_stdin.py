#!/usr/bin/env python3

import sys

def main():
	ans = 0.0
	for line in sys.stdin:
		ans += float(line)
	print(ans)


if __name__ == '__main__':
	main()
