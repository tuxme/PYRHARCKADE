#!/bin/bash

ROM_PATH=/home/pi/EXPORT/MAME/roms
BIN_MAME=/home/pi/mame4all-pi/mame
BIN_FBA=/home/pi/emulators/fba/fba2x
FILE_OK=/tmp/MAME_OK.txt
FILE_TO_COMPLETE=/tmp/MAME_TO_COMPLETE


rm -f $FILE_OK
rm -f $FILE_TO_COMPLETE



echo "GENERATE MAME/FBA ROM LISTE"

$BIN_FBA --gamelist 

cd $ROM_PATH
for rom in `ls -1 *zip | cut -d"." -f1`
	do
		DATA=`$BIN_MAME -verifyroms $rom`
		STATUS=$?
		if [[ "$STATUS" == "0" ]]
			then
				echo "$rom,MAME" >> $FILE_OK
		fi
		

		if [[ "$STATUS" == "2" ]]
			then

				echo -e "-------- ${rom}\n$DATA" >> $FILE_TO_COMPLETE
		fi
		if [[ "$STATUS" == "1" ]]
			then
				echo "$rom : NOT SUPORTED"
		fi
		for fba_rom in `cat /home/pi/emulators/fba/gamelist.txt  | cut -d" " -f2 | grep $rom`

			do
				if [[ $STATUS != "0" ]]
					then
						echo "$fba_rom,FBA" | tee -a /tmp/FBA_OK
				fi
			done			

	done


cat  /tmp/FBA_OK $FILE_OK | sort -d | sort -u >> /tmp/ROM_CONFIG_FILES.csv

echo "
--------------------------------------------------------
the file of all your conf for MAME and FBA is :
	/tmp/ROM_CONFIG_FILES.csv

if you want to verify the rom who could work but are not complete see the file :
	$FILE_TO_COMPLETE
	(the command to retry is : $BIN_MAME -verifyroms [YOUR ROM]

"

