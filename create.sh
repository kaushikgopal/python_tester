#!/usr/bin/env bash

# run this like so ./create.sh "prime_number"
echo "argument is $1"
mkdir -p $1
cd $1
cp ../logic*.py .
mv logic.py $1_logic.py
mv logic_test.py $1_test.py

# code .