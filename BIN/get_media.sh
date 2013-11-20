#!/bin/bash

usage() {

echo "$0 : Recupere les medias de type information / snapshoot / wheel selon votre fichier ROM_CONFIG_FILES.csv"
echo ""
echo "OPTION : "
echo "		$0 --> recupere tout les medias"
echo "		$0 [rom] --> recupere tout les medias d'une rom particuliere en mode FORCE (ecrase l'existant)"
echo "		$0 ALL --> recupere tout les medias de toutes les ROMS en  mode FORCE (ecrase l'existant)"
exit

}

for var in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
	do

		
		if [[ ! -z $1 ]]
			then
				if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]
					then
						usage
				fi
				if [[ "$1" == "ALL" ]]
					then 
						FORCE_ALL=1
					else
						FORCE=1
						var=$1
				fi
			else
				FORCE=0
				FORCE_ALL=0
		fi
		echo "Traitement de $var -  "
		if [[ ! -f ../MEDIA/DOCS/${var}.txt ]] || [[ "$FORCE_ALL" == "1"  ]] || [[ "$FORCE" == "1" ]]
			then
				echo "ROM_NAME: $var" > ../MEDIA/DOCS/${var}.txt
				wget -c -q http://occultaleges.eu/PYRHARCKADE/MEDIA/DOCS/${var}.txt -O ../MEDIA/DOCS/${var}.txt
				RES=$?
				if [[ "$RES" != "0" ]]
					then
						echo -e "$var \n * NO DATA INFORMATION" > ../MEDIA/DOCS/${var}.txt
						echo -e "\t(DOC): FAILED"
					else
						echo -e "\t(DOC): OK"
				fi
		fi
		if [[ ! -f "../MEDIA/SNAP/${var}.png" ]] || [[ "$FORCE_ALL" == "1"  ]] || [[ "$FORCE" == "1" ]]
			then
				TEST_OK=0
				for type in snap marquee title
					do
						if [[ "$TEST_OK" == "0" ]]
							then
								wget -c -q -nv "http://occultaleges.eu/PYRHARCKADE/MEDIA/${type}/${var}.png" -O ../MEDIA/SNAP/${var}.png
								RES=$?
							if [[ "$RES" == "0" ]]
								then
									TEST_OK=1
									echo -e "\t(SNAP): OK"
							fi 
						fi
					done
				if [[ "$TEST_OK" == "0" ]]
					then
						echo -e "\t(SNAP): FAILED"
						rm -f ../MEDIA/SNAP/${var}.png
				fi
		fi
		if [[ ! -f "../MEDIA/WHEEL/${var}.png" ]] || [[ "$FORCE_ALL" == "1"  ]] || [[ "$FORCE" == "1" ]]
			then
				wget -c -q -nv "http://occultaleges.eu/PYRHARCKADE/MEDIA/wheel/${var}.png" -O ../MEDIA/WHEEL/${var}.png
				if [[ "$?" == "0" ]]
					then
						echo -e "\t(WHEEL): OK"
					else
						wget -c -q -nv "http://occultaleges.eu/PYRHARCKADE/MEDIA/lowres/${var}.png" -O ../MEDIA/WHEEL/${var}.png
						if [[ "$?" == "0" ]]
							then
								echo -e "\t(WHEEL): OK"
							else
								NAME=`cat ../MEDIA/DOCS/${var}.txt |grep Name | cut -d":" -f2`
								if [[ ! -z "$NAME" ]]
									then
										wget -c -q "http://placehold.it/400x175/000000/FFFFFFF/&text=${NAME}" -O /tmp/${var}.png
									else
										wget -c -q "http://placehold.it/400x175/000000/FFFFFFF/&text=${var}" -O /tmp/${var}.png
								fi
								rm -f ../MEDIA/WHEEL/${var}.png
								convert -border 4x4 -bordercolor "#FFFFFF" /tmp/${var}.png ../MEDIA/WHEEL/${var}.png 
								echo  -e "\t(WHEEL): CONVERT"
						fi
				fi
				
		fi

		echo "-------------------------------"

	if [[ ! -z $1 ]] && [[ "$1" != "ALL" ]]
		then
			exit
	fi
 done
