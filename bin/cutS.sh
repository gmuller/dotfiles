#!/bin/bash

dur=$(soxi -D "$1")
length=$(echo "scale=6; $dur/$2" | bc)

file=$(basename "$1")
file="${file%.*}"

a=0
while [ $a  -lt "$2" ]
do
  start=$(echo "scale=6; $a*$length" | bc -l)

  if [ $a -lt 10 ]
  then
    outfile=($file-0$a.wav)
  else
    outfile=($file-$a.wav)
  fi

  sox $1 $outfile trim $start $length

  end=$(echo "scale=6; $start+$length" | bc)
  echo "done: $outfile start: $start end: $end"
  a=`expr $a + 1`
done
