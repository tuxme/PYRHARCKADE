#!/bin/bash

####### CONF ########
ROM=$1
SCREEN=$2
PATH_ROMS=${HOME}/PYRHARCKADE/ROMS/FBA/
BIN_MAME=/home/pi/emulators/fba/fba2x
####### CONF ########

cd ${PATH_ROMS}/
${BIN_MAME} $ROM

###### RESTART PYR ######
cd ${HOME}/PYRHARCKADE/
./start.py YES $SCREEN
###### RESTART PYR ######
