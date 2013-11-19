#!/bin/bash

if [[ -z $1 ]]
	then
		for rom in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
			do
				echo "Generate $rom ..."
				curl -sq "http://www.mamedb.com/game/${rom}" | grep "<h1>Game Details</h1>" | html2text | grep -B 50 "Input" | grep -v Input | grep -v "Game Details" > ../MEDIA/DOCS/${rom}.txt
				if [[ ! -z `file ../MEDIA/DOCS/${rom}.txt | grep empty` ]]
					then
						echo -e "$rom \n * NO DATA INFORMATION" > ../MEDIA/DOCS/${rom}.txt
				fi
			done
	else
		rom=$1
		echo "Generate $rom ..."
		curl -sq "http://www.mamedb.com/game/${rom}" | grep "<h1>Game Details</h1>" | html2text | grep -B 50 "Input" | grep -v Input | grep -v "Game Details" > ../MEDIA/DOCS/${rom}.txt
		if [[ ! -z `file ../MEDIA/DOCS/${rom}.txt | grep empty` ]]
			then
				echo -e "$rom \n * NO DATA INFORMATION" > ../MEDIA/DOCS/${rom}.txt
		fi

fi
