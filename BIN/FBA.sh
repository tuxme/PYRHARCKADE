#!/bin/bash

####### CONF ########
ROM=$1
PATH_ROMS=${HOME}/PYRHARCKADE/ROMS/FBA/
BIN_MAME=/home/pi/emulators/fba/fba2x
####### CONF ########

cd ${PATH_ROMS}/
${BIN_MAME} $ROM

###### RESTART PYR ######
cd ${PATH_ROMS}/../../
./start.py YES
###### RESTART PYR ######
