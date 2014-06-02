#!/bin/bash

####### CONF ########
ROM=$1
PATH_ROMS=${HOME}/PYRHARCKADE/ROMS/MAME/
BIN_MAME=/usr/games/mame
####### CONF ########

cd ${PATH_ROMS}/
${BIN_MAME} $ROM

###### RESTART PYR ######
cd ${PATH_ROMS}/../
./start.py YES
###### RESTART PYR ######	
