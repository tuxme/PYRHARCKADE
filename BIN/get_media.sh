#!/bin/bash

ROM_ARG=$1

usage() {

echo "$0 : 	Recupere les medias de type information / snapshoot / wheel selon votre fichier ROM_CONFIG_FILES.csv"
echo "		Recupere aussi les ROMS MAME et FBA si elles existent sur le serveur"	
echo ""	
echo "---	Dans un premier temps nous vous conseillons de mettre les emulateur FBA et MAME à MAME puis de lancer "
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
			rm -f ../MEDIA/${EMU}/DOCS/${ROM}.txt
			echo -e " -> DOCS \033[31m FAILED \033[0m"
		else
			echo -e " -> DOCS \033[32m SUCCESS \033[0m"

	fi

}

get_snap() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/SNAP/${ROM}.png" -O ../MEDIA/${EMU}/SNAP/${ROM}.png
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm -f ../MEDIA/${EMU}/SNAP/${ROM}.png
			cp -f ../MEDIA/no_snap.png ../MEDIA/${EMU}/SNAP/${ROM}.png
			echo -e " -> SNAP \033[31m FAILED \033[0m"
		else
			echo -e " -> SNAP \033[32m SUCCESS \033[0m"
	fi

}

get_wheel() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/WHEEL/${ROM}.png" -O ../MEDIA/${EMU}/WHEEL/${ROM}.png
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm -f ../MEDIA/${EMU}/WHEEL/${ROM}.png
			cp -f ../MEDIA/no_wheel.png ../MEDIA/${EMU}/WHEEL/${ROM}.png
			echo -e " -> WHEEL \033[31m FAILED \033[0m"
		else
			echo -e " -> WHEEL \033[32m SUCCESS \033[0m"
	fi

}
get_video() {
	wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/${EMU}/VIDEO/${ROM}.mpg" -O ../MEDIA/${EMU}/WHEEL/${ROM}.png
	RES=$?
	if [[ "$RES" != "0" ]]
		then
			rm -f ../MEDIA/${EMU}/VIDEO/${ROM}.png
			echo -e " -> VIDEO \033[31m FAILED \033[0m"
		else
			echo -e " -> VIDEO \033[32m SUCCESS \033[0m"
	fi

}

get_roms() {
	if [[ "${EMU}" -eq "MAME" ]] || [[ "${EMU}" -eq "FBA" ]] 
		then
			EMU="MAME"
			wget -c -q -nv "http://pyrharckade.tuxme.net/MEDIA/roms/MAME_37B5/${ROM}.zip" -O ../ROMS/${EMU}/${ROM}.zip
			RES=$?
			if [[ "$RES" != "0" ]]
				then
					rm -f  ../ROMS/${EMU}/${ROM}.zip
				echo -e " -> ROMS \033[31m FAILED \033[0m"
			else
				echo -e " -> ROMS \033[32m SUCCESS \033[0m"
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
		get_video
		get_docs
		get_roms
		exit 0
fi

while read line 
	do
		echo $line | while IFS=',' read ROM EMU
		do
			echo -e "----- \033[36m $ROM \033[0m -----"
			get_snap
			get_wheel
			get_video
			get_docs
			get_roms	
		done
done < ../ROM_CONFIG_FILES.csv 

