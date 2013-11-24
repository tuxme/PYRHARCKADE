#!/bin/bash

ROM=$1

cd /home/pi/EXPORT/MAME/roms/
/home/pi/mame4all-pi/mame $ROM 

cd /home/pi/PYRHARCKADE
./start.py YES
