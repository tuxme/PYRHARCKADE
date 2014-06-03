#!/bin/bash

if [[ "$1" == "REBOOT" ]]
	then
		sudo reboot
fi

if [[ "$1" == "HALT" ]]
	then
		sudo halt
fi
exit
