Files:
  parser.sh : shell script parsing data
  bio.py : python code which deal with parsed data to generate the chart
  <input filename> : a file which you may want to parse using the shell script
  <parsed result filename> : expected output file name
  <range(base) of ChrPos> : range or base of chromosome position you may concern (i.e. 1000000(mega) base)

How to run:
  1. parse the data, removing all obsolete columns
     ./parser.sh <input filename> <parsed result filename>
     i.e. ./parse.sh total.txt parsed_total.txt
  
  2. run the program with parsed result
     python bio.py <parsed result filename> <range(base) of ChrPos>
     i.e. python bio.py parsed_total.txt 1000000
