#!/bin/bash

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

ng () {
	echo "NG in line $1"
	ret=1
}

ret=0

out=$(./dice.py)
[ "${out}" = "need 1 or 2 arguments" ] || ng ${LINENO}

arg1=a
out=$(./dice.py ${arg1})
[ "${out}" = "1st argument must be integer" ] || ng ${LINENO}

arg1=-1
out=$(./dice.py ${arg1})
[ "${out}" = "1st argument must be in [1,10]" ] || ng ${LINENO}

arg1=10
arg2=5
out=$(./dice.py ${arg1} ${arg2})
[ "${out}" = "5 3 6 3 6 6 6 5 1 4" ] || ng ${LINENO}

exit ${ret}

