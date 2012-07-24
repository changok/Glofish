#!/bin/bash

cat $1 
  | sed '/^"mutantID"/ d' 
  | sed '/^""/ d' 
  | sed 's/"[0-9]*" \("mutant_[1-9]*"\) \("[I,V,X]*"\) .* \([0-9]*\) .* \([0-9]*\) \([0-9]*\) .*/\1 \2 \3/' 
  | sed 's/"//g' 
  | sed 's/mutant_//g' 
  > $2
