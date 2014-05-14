#!/bin/bash

ROM_ARG=$1

usage() {

echo "$0 : 	Recupere les medias de type information / snapshoot / wheel selon votre fichier ROM_CONFIG_FILES.csv"
echo "		Recupere aussi les ROMS MAME et FBA si elles existent sur le serveur"	
echo ""	
echo "---	Dans un premier temps nous vous conseillons de mettre les emulateur FBA et MAME à MAME puis de lancer "
ehco "---	verif_roms.sh qui fera les test des ROMS et generera un nouveau fichier de conf	"	
echo ""	
echo "OPTION : "
echo "		$0 --> recupere tout les medias"
echo "		$0 \"[rom],[EMU]\" --> recupere tout les medias d'une rom particuliere en mode FORCE (ecrase l'existant)"
exit

}

test_arg() {
EMU=`echo $ROM_ARG | cut -d"," -f2`
ROM=`echo $ROM_ARG | cut -d"," -f1`

if [[ -z $EMU ]] || [[ -z $ROM ]] || [[ -z `echo $ROM_ARG | grep ","` ]]
	then
		usage

fi

}

TEST_REP() {

if [[ ! -z $ROM_ARG ]]
	then 
		if [[ ! -d ../MEDIA/${EMU}/SNAP ]]
			then
				echo "Creation rep IMG de ${EMU} : ../MEDIA/${EMU}/SNAP"
				mkdir -p ../MEDIA/${EMU}/SNAP
		fi
		if [[ ! -d ../MEDIA/${EMU}/WHEEL ]]
			then
				echo "Creation rep IMG de ${EMU} : ../MEDIA/${EMU}/WHEEL"
				mkdir -p ../MEDIA/${EMU}/WHEEL
		fi
		if [[ ! -d ../MEDIA/${EMU}/DOCS ]]
			then
				echo "Creation rep IMG de ${EMU} : ../MEDIA/${EMU}/DOCS"
				mkdir -p ../MEDIA/${EMU}/DOCS
		fi
		if [[ ! -d ../ROMS/${EMU}/ ]]
			then
				echo "Creation rep ROMS de ${EMU} : ../ROMS/${EMU}/"
				mkdir -p ../ROMS/${EMU}/
		fi
	else

		for EMU_DIR in `cat ../ROM_CONFIG_FILES.csv | cut -d"," -f2 | sort -u`
			do
				if [[ ! -d ../MEDIA/${EMU_DIR}/SNAP ]]
					then
						echo "Creation rep IMG de ${EMU_DIR} : ../MEDIA/${EMU_DIR}/SNAP"
						mkdir -p ../MEDIA/${EMU_DIR}/SNAP
				fi
				if [[ ! -d ../MEDIA/${EMU_DIR}/WHEEL ]]
					then
						echo "Creation rep IMG de ${EMU_DIR} : ../MEDIA/${EMU_DIR}/WHEEL"
						mkdir -p ../MEDIA/${EMU_DIR}/WHEEL
				fi
				if [[ ! -d ../MEDIA/${EMU_DIR}/DOCS ]]
					then
						echo "Creation rep IMG de ${EMU_DIR} : ../MEDIA/${EMU_DIR}/DOCS"
						mkdir -p ../MEDIA/${EMU_DIR}/DOCS
				fi
				if [[ ! -d ../ROMS/${EMU_DIR}/ ]]
					then
						echo "Creation rep ROMS de ${EMU_DIR} : ../ROMS/${EMU_DIR}/"
						mkdir -p ../ROMS/${EMU_DIR}/
				fi
			done
fi

}
get_docs() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/DOCS/${ROM}.txt" -O ../MEDIA/${EMU}/DOCS/${ROM}.txt
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm ../MEDIA/${EMU}/DOCS/${ROM}.txt
			echo "$ROM $EMU -> DOCS : FAILED"
	fi

}

get_snap() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/SNAP/${ROM}.png" -O ../MEDIA/${EMU}/SNAP/${ROM}.png
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm ../MEDIA/${EMU}/SNAP/${ROM}.png
			echo "$ROM $EMU -> SNAP : FAILED"
	fi

}

get_wheel() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/WHEEL/${ROM}.png" -O ../MEDIA/${EMU}/WHEEL/${ROM}.png
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm ../MEDIA/${EMU}/WHEEL/${ROM}.png
			echo "$ROM $EMU -> WHEEL : FAILED"
	fi

}

get_roms() {
	if [[ "${EMU}" -eq "MAME" ]] || [[ "${EMU}" -eq "FBA" ]] 
		then
			EMU="MAME"
			wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/roms/MAME_151/${ROM}.zip" -O ../ROMS/${EMU}/${ROM}.zip
			RES=$?
			if [[ "$RES" != "0" ]]
				then
					rm  ../ROMS/${EMU}/${ROM}.zip
					echo "$ROM $EMU -> ROMS : FAILED"
			fi
	fi

}



if [[ -z $ROM_ARG ]]
	then
	TEST_REP
fi


if [[ ! -z $ROM_ARG ]]
	then
		test_arg
		TEST_REP
		get_snap
		get_wheel
		get_docs
		get_roms
		exit 0
fi

while read line 
	do
		echo $line | while IFS=',' read ROM EMU
		do

			get_snap
			get_wheel
			get_docs
			get_roms

				
		done
done < ../ROM_CONFIG_FILES.csv 

