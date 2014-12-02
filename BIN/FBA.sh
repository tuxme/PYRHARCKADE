#!/bin/bash

####### CONF ########
ROM=$1
SCREEN=$2
PATH_ROMS=${HOME}/PYRHARCKADE/MEDIA/FBA/ROMS/
BIN_MAME=/home/pi/pimame/emulators/fba/fba2x
####### CONF ########

cd `dirname $BIN_MAME`
${BIN_MAME} roms/${ROM}.zip


###### RESTART PYR ######
cd ${HOME}/PYRHARCKADE/
./start.py YES $SCREEN
###### RESTART PYR ######
