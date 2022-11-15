#!/bin/bash

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

ng () {
  echo "NG in line $1"
  ret=1
}

ret=0

out=$(diff <(cat robosys2022.txt) <(./show_robosys.py))
[ $? -eq 0 ] || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}


exit ${ret}
