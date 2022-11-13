#!/bin/bash

# SPDX-FileCopyrightText: 2022 ShinagwaKazemaru
# SPDX-FileCopyrightIdentifer: MIT License

ng () {
  echo "NG in line $1"
  ret=1
}

ret=0

diff <(cat aas_test_expected_output.txt) <(./aas_test.py sample)
[ $? -eq 0 ] || ng ${LINENO}

exit ${ret}
