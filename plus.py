#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

import sys

def main():
	ans = 0
	for line in sys.stdin:
		try:
			ans += int(line)
		except:
			ans += float(line)
	print(ans)


if __name__ == '__main__':
	main()
