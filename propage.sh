#!/bin/bash

IP=192.168.0.9
git add .
git commit -m "update `date +%s`"
git push
echo "RM de  pi@${IP} /home/pi/PYRHARCKADE/"
ssh pi@${IP} "rm -Rf /home/pi/PYRHARCKADE/"
echo "scp "
scp -r ~/PYRHARCKADE/ pi@${IP}:
