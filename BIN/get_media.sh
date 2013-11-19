#!/bin/bash

for var in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
	do
		if [[ ! -f "../MEDIA/SNAP/${var}.png" ]]
			then
				echo -n "Traitement de $var : "
				TEST_OK=0
				for type in snap marquee title
					do
						if [[ "$TEST_OK" == "0" ]]
							then
								wget -c -q -nv "http://occultaleges.eu/deadpool/DATA_FE_PYRHARCKADE/${type}/${var}.png " -O ../MEDIA/SNAP/${var}.png
							if [[ "$?" == "0" ]]
								then
									TEST_OK=1
									echo -n "(SNAP): OK"
							fi 
						fi
					done
				if [[ "$TEST_OK" == "0" ]]
					then
						echo -n "(SNAP): FAILED"
						rm -f ../MEDIA/SNAP/${var}.png
				fi
				if [[ -f "../MEDIA/WHEEL/${var}.png" ]]
					then
						echo ""
				fi
		fi
		if [[ ! -f "../MEDIA/WHEEL/${var}.png" ]]
			then
				wget -c -q -nv "http://occultaleges.eu/deadpool/DATA_FE_PYRHARCKADE/wheel/${var}.png" -O ../MEDIA/WHEEL/${var}.png
				if [[ "$?" == "0" ]]
					then
						echo  " (WHEEL): OK"
					else
						echo  " (WHEEL): FAILED"
						rm -f ../MEDIA/WHEEL/${var}.png
				fi
				
		fi
 done
