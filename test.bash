#!/bin/bash
# SPDX-FileCopyrightText: 2022 Shinagawa Kazemaru
# SPDX-FileCopyrightIdentifer: MIT License

ng () {
	echo NG in Line $1
	res=1
}

res=0

out=$(seq 5 | ./plus.py)
[ "${out}" = 14 ] || ng ${LINENO}

out=$(echo あ | ./plus.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}

out=$(echo | ./plus.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}

[ "$res" = 0 ] && echo OK
exit $res
