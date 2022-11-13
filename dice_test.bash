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
#[ "${out}" = "5 3 6 3 6 6 6 5 1 4" ] || ng ${LINENO}

diff <(cat dice_expected_output.txt) <(echo "${out}")
[ $? = 0 ] || ng ${LINENO}

<< comment
ng_output (){
  echo "different output @ line $1"
  ret=1
}

#echo ${out}
IFS=$'\n'
dices_lines=(${dices})
out_lines=(${out})
echo ${dices_lines[1]}
echo ${out_lines[1]}
[ ${out_lines[1]} = ${dices_lines[1]} ] && echo "match!!" || echo "different..."
if [ ${#out_lines[*]} -eq ${#dices_lines[*]} ] ; then
  n=${#out_lines[*]}
  for ((i=0; i < ${n}; i++)); do
    [ ${out_lines[${i}]} = ${dices_lines[${i}]} ] || ng_output ${i}+1
  done
else
  ng ${LINENO}
fi
comment

exit ${ret}

