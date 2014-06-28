#!/bin/bash

DIR_CONVERT=$1

if [[ ! -d $DIR_CONVERT ]]
	then
		echo "Select a valid dir"
		exit
fi

cd $DIR_CONVERT
if [[ ! -d CONVERT_FILE_MPG ]]
	then
		mkdir CONVERT_FILE_MPG
fi
for var in `ls -1 | grep -v CONVERT_FILE_MPG |  cut -d"." -f1`
	do
		if [[ -f "CONVERT_FILE_MPG/${var}.mpg" ]]
			then
				echo "File exist"
			else
				ffmpeg -i ${var}.mp4 -target ntsc-vcd    CONVERT_FILE_MPG/${var}.mpg
		fi
	done
