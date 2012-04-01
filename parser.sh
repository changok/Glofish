#!/bin/bash

cat interRank.txt | sed '/^"mut/ d' | sed 's/"[0-9]*" \("mutant_[1-8]"\) .* \([0-9]*\) ".*" .*/\1 \2/' | sed 's/"//g' | sed 's/mutant_//g' > parsedRank.txt
