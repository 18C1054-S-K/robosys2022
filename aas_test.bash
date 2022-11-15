#!/bin/bash

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

ng () {
  echo "NG in line $1"
  ret=1
}

ret=0

out=$(./aas_test.py あ)
[ $? -eq 1 ] || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}

out=$(diff <(cat aas_test_expected_output.txt) <(./aas_test.py robosys2022))
[ $? -eq 0 ] || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}

out=$(diff <(cat robosys2022.txt) <(./show_robosys.py))
[ $? -eq 0 ] || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}


exit ${ret}
