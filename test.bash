#!/bin/bash

out=$(seq 5 | ./plus.py)

[ "${out}" = 14 ]
