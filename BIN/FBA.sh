exec 1>/home/pi/PYRHARCKADE/BIN/log1
exec 2>/home/pi/PYRHARCKADE/BIN/log2
#!/bin/bash

####### CONF ########
ROM=$1
SCREEN=$2
PATH_ROMS=${HOME}/PYRHARCKADE/MEDIA/FBA/FBA/roms/
BIN_FBA=/home/pi/PYRHARCKADE/MEDIA/FBA/FBA/fba2x
####### CONF ########
cd ${PATH_ROMS}/
${BIN_FBA} /home/pi/PYRHARCKADE/MEDIA/FBA/FBA/roms/$ROM.zip

###### RESTART PYR ######
cd ${HOME}/PYRHARCKADE/
./start.py YES $SCREEN
###### RESTART PYR ######
