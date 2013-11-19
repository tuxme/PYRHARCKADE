#!/bin/bash

if [[ -z $1 ]]
	then
		for rom in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
			do
				echo "Generate $rom ..."
				echo "ROM_NAME: $rom" > ../MEDIA/DOCS/${rom}.txt
				curl -sq "http://www.mamedb.com/game/${rom}" | grep '<h1>Game Details</h1>'| sed "s#<#\n<#g"| sed "s#>#>\n#g" | grep -A70 'Game Details' | html2text  | grep -v 'Game Details' | grep -v "Filename">> ../MEDIA/DOCS/${rom}.txt
				if [[ ! -z `file ../MEDIA/DOCS/${rom}.txt | grep empty` ]]
					then
						echo -e "$rom \n * NO DATA INFORMATION" > ../MEDIA/DOCS/${rom}.txt
				fi
			done
	else
		rom=$1
		echo "Generate $rom ..."
		echo "ROM_NAME: $rom" > ../MEDIA/DOCS/${rom}.txt	
		curl -sq "http://www.mamedb.com/game/${rom}" | grep '<h1>Game Details</h1>'| sed "s#<#\n<#g"| sed "s#>#>\n#g" | grep -A70 'Game Details' | html2text  | grep -v 'Game Details'  >> ../MEDIA/DOCS/${rom}.txt
		if [[ ! -z `file ../MEDIA/DOCS/${rom}.txt | grep empty` ]]
			then
				echo -e "$rom \n * NO DATA INFORMATION" > ../MEDIA/DOCS/${rom}.txt
		fi

fi
