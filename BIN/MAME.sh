#!/bin/bash

####### CONF ########
ROM=$1
PATH_ROMS=${HOME}/PYRHARCKADE/MEDIA/MAME/ROMS/
BIN_MAME=/home/pi/pimame/emulators/mame4all-pi/mame
####### CONF ########

cd ${PATH_ROMS}/
${BIN_MAME} $ROM

###### RESTART PYR ######
cd ${PATH_ROMS}/../
./start.py YES
###### RESTART PYR ######	
