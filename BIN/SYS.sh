#!/bin/bash

if [[ "$1" == "001_REBOOT" ]]
	then
		sudo reboot
		exit
fi

if [[ "$1" == "001_HALT" ]]
	then
		sudo halt
		exit
fi

if [[ "$1" == "001_MEDIA" ]]
	then
		cd BIN
		./get_media.sh
		cd ../
		./start.py YES

fi
if [[ "$1" == "001_VERIF" ]]
	then
		cd BIN
		./verif_roms.sh
		cd ../
		./start.py YES

fi






