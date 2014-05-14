#!/bin/bash

####### CONF ########
ROM=$1
PATH_ROMS=${HOME}/PYRHARCKADE/ROMS/
BIN_MAME=/home/pi/mame4all-pi/mame
####### CONF ########


cd ${PATH_ROMS}/
${BIN_MAME} $ROM

###### RESTART PYR ######
cd ${PATH_ROMS}/../
./start.py YES
###### RESTART PYR ######
