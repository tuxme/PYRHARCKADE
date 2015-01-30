exec 2>/home/pi/PYRHARCKADE/BIN/log2
#!/bin/bash

####### CONF ########
ROM=$1
SCREEN=$2
PATH_ROMS=/home/pi/gngeo-pi/roms/
BIN_GNGEO=/home/pi/gngeo-pi/bin/gngeo
####### CONF ########

cd ${PATH_ROMS}/
${BIN_GNGEO} $ROM

###### RESTART PYR ######
cd ${HOME}/PYRHARCKADE/
./start.py YES $SCREEN
###### RESTART PYR ######	
