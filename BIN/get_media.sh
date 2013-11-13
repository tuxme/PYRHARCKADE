#!/bin/bash

for var in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f1`
	do
		if [[ ! -f "../MEDIA/SNAP/${var}.png MEDIA/WHEEL/" ]]
			then
				echo -n "Traitement de $var : "
				for type in snap marquee title
					do
						TEST_OK=0
						wget -c -q -nv "http://www.mamedb.com/${type}/${var}.png" -O ../MEDIA/SNAP/${var}.png
						if [[ "$?" == "0" ]]
							then
								TEST_OK=1
								break
						fi
					done
				if [[ "$TEST_OK" == "1" ]]
					then
						echo -n "(SNAP): OK"
					else
						echo -n "(SNAP): FAILED"
						rm -f ../MEDIA/SNAP/${var}.png
				fi
		fi
		if [[ ! -f "../MEDIA/SNAP/${var}.png MEDIA/WHEEL/" ]]
			then
				wget -c -q -nv "http://occultaleges.eu/deadpool/DATA_FE_PYRHARCKADE/wheel/${var}.png" -O ../MEDIA/WHEEL/${var}.png
				if [[ "$?" == "0" ]]
					then
						echo -n " (WHEEL): OK"
					else
						echo -n " (WHEEL): FAILED"
						rm -f ../MEDIA/WHEEL/${var}.png
				fi
				
		fi
	echo ""
 done
