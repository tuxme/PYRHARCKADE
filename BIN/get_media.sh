#!/bin/bash


for var in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
	do

		
		if [[ ! -z $1 ]]
			then
			var=$1
		fi
		echo "Traitement de $var -  "
		if [[ ! -f ../MEDIA/DOCS/${var}.txt ]]
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
		if [[ ! -f "../MEDIA/SNAP/${var}.png" ]]
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
		if [[ ! -f "../MEDIA/WHEEL/${var}.png" ]]
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
								NAME=`cat ../DOC/${var}.txt |grep Name | cut -d":" -f2`
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

	if [[ ! -z $1 ]]
		then
			exit
	fi
 done
