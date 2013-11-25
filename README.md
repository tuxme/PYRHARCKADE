PYRHARCKADE
===========


http://pyrharckade.tuxme.net/

Front end Python mame / neogeo / nes / sega ...

1/ Media are not present . There is some example but not all .
	WHEEL	: are the title
	SNAP	: are the snapshot in game
	DOCS	: are the file wich contains information about game
		  You have to launch in the directory BIN/ the script ./generate_info.sh 
	SOUND	: The bip :)

2/ The script are not present in BIN/ . there are some exmaples.

3/ ALL the script in BIN/EMULATEUR.sh have to finish by:

	cd /home/pi/PYRHARCKADE
	./start.py YES

	To loop (python use a lot of memory so when you launch a game it kill python and start the script . When the script is finich it launch python 

4/ All the configuration is in ROM_CONFIG_FILES.csv
	ROM,EMULATEUR

5/ It is the first version... so be quit and take some bear :)

