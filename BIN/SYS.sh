#!/bin/bash

if [[ "$1" == "REBOOT" ]]
	then
		sudo reboot
		exit
fi

if [[ "$1" == "HALT" ]]
	then
		sudo halt
		exit
fi

if [[ "$1" == "MEDIA" ]]
	then
		cd BIN
		./get_media.sh
		cd ${PATH_ROMS}/../
		./start.py YES

fi



