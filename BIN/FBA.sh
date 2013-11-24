ROM=$1.zip
echo $ROM
cd /home/pi/EXPORT/MAME/roms/
/home/pi/emulators/fba/fba2x  /home/pi/EXPORT/MAME/roms/$ROM 

cd /home/pi/PYRHARCKADE
./start.py YES
