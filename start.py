#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Dead Front Pool Head  is a simple pygame front for PIMAME
# version: 0.1
# guillaume@tuxme.net
# GPL Licence


import pygame
from pygame.locals import *
from Tkinter import*
import time
import csv
import os
import sys
import re
import subprocess
from PIL import Image
from pygame.locals import *
from math import *
from subprocess import Popen


pygame.init()



#CONFIG ###############################################

ROOT_HOME=(os.environ['HOME'] + "/PYRHARCKADE")
BIN_PATH=(ROOT_HOME + "/BIN/")
WHEEL=(ROOT_HOME + "/MEDIA/WHEEL/")
SNAP=(ROOT_HOME + "/MEDIA/SNAP/")
ROMS=(ROOT_HOME + "/MEDIA/ROMS/")
DOCS=(ROOT_HOME + "/MEDIA/DOCS/")
IMG=(ROOT_HOME + "/MEDIA/IMG/")
BACKGROUNG=(ROOT_HOME + "/MEDIA/IMG/bg2.png")
BACKGROUNG_ORIG=(ROOT_HOME + "/MEDIA/IMG/bg2_orig.png")
BACKGROUNG_START=(ROOT_HOME + "/MEDIA/IMG/dpfe_welcom.png")
font = pygame.font.SysFont("comicsansms", 35)
root = Tk()

#TEMPLATE ##############################################

SCREEN_W = root.winfo_screenwidth()
SCREEN_H = root.winfo_screenheight()
SIZE_SNAP_CONVERT_W = int(floor(SCREEN_W / 6))
SIZE_SNAP_CONVERT_H = int(floor(SCREEN_H / 2.5))
SIZE_SNAP_CONVERT=(SIZE_SNAP_CONVERT_W,SIZE_SNAP_CONVERT_H)
SIZE_WHEEL_CONVERT_W = SIZE_SNAP_CONVERT_W
SIZE_WHEEL_CONVERT_H = int(floor(SIZE_WHEEL_CONVERT_W / 2))
SIZE_WHEEL_CONVERT=(SIZE_WHEEL_CONVERT_W,SIZE_WHEEL_CONVERT_H)

SEPARATION_WHEEL_SNAP = 10

WHERE_WHEEL_X = SIZE_WHEEL_CONVERT_W
WHERE_WHEEL_Y = int(floor(SCREEN_H / 8))
WHERE_WHEEL=(WHERE_WHEEL_X,WHERE_WHEEL_Y)
WHERE_SNAP_X = SIZE_WHEEL_CONVERT_W
WHERE_SNAP_Y = WHERE_WHEEL_Y + SIZE_WHEEL_CONVERT_H + SEPARATION_WHEEL_SNAP
WHERE_SNAP=(WHERE_SNAP_X,WHERE_SNAP_Y)
WHERE_TEXTE_X = int(floor(WHERE_WHEEL_X * 3))
WHERE_TEXTE_Y = int(floor(SCREEN_H / 3))
WHERE_TEXTE=(WHERE_TEXTE_X,WHERE_TEXTE_Y)
WHERE_BIN_X = SCREEN_W  - WHERE_SNAP_X - int(floor(WHERE_SNAP_X/4))
WHERE_BIN_Y =  WHERE_SNAP_Y

########################################################

#FENETRE PRINCIPAL #####################################
fenetre = [SCREEN_W, SCREEN_H]
fenetre = pygame.display.set_mode((fenetre),FULLSCREEN)
fenetre.blit(pygame.transform.scale(pygame.image.load(IMG + "/bg2.png").convert_alpha(),(SCREEN_W,SCREEN_H)),(0,0))


#COMPTEUR et lecture du fichier conf ###################
CPT = 0
MAX = 0
reader = csv.reader(file(ROOT_HOME + "/ROM_CONFIG_FILES.csv" ))
li = []
for row in reader:
        li.append(row)
	MAX = MAX +1	
NMAX=(MAX * -1) +1 
MAX = MAX -1
FIRST=1
continuer = 1
#######################################################
# Initialisation / ou non du joystick 0
if pygame.joystick.get_count() != 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init()
	JOY_TEST = 1
	print "----- Joy OK"
else:
	JOY_TEST = 0
#delay = 100
neutral = True
pressed = 0
#last_update = pygame.time.get_ticks()









def affiche():
	# Formatage du nom en iamge avec path complet	
	IMG_WHEEL=WHEEL +li[CPT][0]+".png"
	IMG_SNAP=SNAP +li[CPT][0]+".png"

	# Affichage des information contenu dans le fichier MEDIA/DOC/[ROM].txt
	FILE_INFO = DOCS + li[CPT][0] + ".txt"
	if os.path.isfile(FILE_INFO):
		FILE_DOC = open(FILE_INFO,"r")
		text1 = FILE_DOC.read()
		text2 = font.render(text1, True, pygame.Color("white"))
		LPLUS=0
		for ligne in text1.splitlines():
			LPLUS=LPLUS + 25
			x,y = fenetre.blit(font.render(ligne,5,pygame.Color("white")),(WHERE_TEXTE_X,WHERE_TEXTE_Y+LPLUS)).bottomleft
		FILE_DOC.close()
	else:
		text1 = "No DATA File"
		text2 = font.render(text1, True, pygame.Color("white"))
		fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y-25)).bottomleft

	# Affichage des SNAP + WHEEL
	if os.path.isfile(IMG_WHEEL):
		fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_WHEEL).convert_alpha(),(SIZE_WHEEL_CONVERT)),(WHERE_WHEEL))
	else:
		fenetre.blit(pygame.transform.scale(pygame.image.load(WHEEL + "no_wheel.png").convert_alpha(),(SIZE_WHEEL_CONVERT)),(WHERE_WHEEL))

	if os.path.isfile(IMG_SNAP):

		fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_SNAP).convert_alpha(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))
	else:
		fenetre.blit(pygame.transform.scale(pygame.image.load(SNAP + "no_snap.png").convert_alpha(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))

	#AFFICHAGE WHEEL
	pygame.display.update()











#MAIN #################################################
pygame.key.set_repeat(400, 30)
while continuer:
	if FIRST == 1:
                fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_START).convert_alpha(),(SCREEN_W,SCREEN_H)),(0,0))
		pygame.display.update()
		FIRST = 0
		time.sleep(1)
	else:

# RESTE AFFICHAGE ####################################
		#Reload du fond pour supprimer convert_alpha #######

		fenetre.fill(pygame.Color("black"))
                fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG).convert_alpha(),(SCREEN_W,SCREEN_H)),(0,0))
		####################################################

		for event in pygame.event.get():
			# Deplacement joystick
			if JOY_TEST == 1:
				if event.type == JOYAXISMOTION:
					#jeux a haut
					if event.axis == 1 and event.value < 0:
						ROM_L1 = li[CPT][0][0]
						ROM_L2 = ROM_L1
						CPT_UP=0
						# Tant que la premiere lettre de la ROM est la meme que la premiere lettre de la ROM + 1
						while ROM_L1 == ROM_L2:
							text1 = "LOADING ..."
							text2 = font.render(text1, True, pygame.Color("white"))
							fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
							CPT_UP = CPT_UP - 1
							if CPT_UP + CPT <= NMAX:
								CPT = 0
							ROM_L1 = li[CPT_UP + CPT][0][0]
						CPT = CPT - CPT_UP
<<<<<<< HEAD
=======
						affiche()
>>>>>>> 64e4282477604e8659d766818bcd2a6d352f8da7
					#jeux a bas
					if event.axis == 1 and event.value > 0:
						ROM_L1 = li[CPT][0][0]
						ROM_L2 = ROM_L1
						CPT_UP=0
						# Tant que la premiere lettre de la ROM est la meme que la premiere lettre de la ROM + 1
						while ROM_L1 == ROM_L2:
							text1 = "LOADING ..."
							text2 = font.render(text1, True, pygame.Color("white"))
							fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
							CPT_UP = CPT_UP + 1
							if CPT_UP + CPT > MAX:
								CPT = 0
							ROM_L1 = li[CPT_UP + CPT][0][0]
						CPT = CPT + CPT_UP
<<<<<<< HEAD
=======
						affiche()
>>>>>>> 64e4282477604e8659d766818bcd2a6d352f8da7
					#jeux a gauche
					if event.axis == 0 and event.value < 0:
						CPT = CPT - 1
						affiche()
					#jeux a droite
					if event.axis == 0 and event.value > 0:
						CPT = CPT + 1
						affiche()
				if event.type == JOYBUTTONDOWN and event.button == 3:
					APP="BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  + " &"
					p = subprocess.Popen(APP, shell=True)
					p.wait()
					#os.system("BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  + " &" )
			# Deplacement clavier
			if event.type == KEYDOWN:
				print str(CPT) + " : " + li[CPT][0]

				#jeux a gauche
				if event.key == K_LEFT:
					CPT = CPT - 1
					affiche()
				#jeux alphabetique +1
				if event.key == K_UP:
					ROM_L1 = li[CPT][0][0]
					ROM_L2 = ROM_L1
					CPT_UP=0
					# Tant que la premiere lettre de la ROM est la meme que la premiere lettre de la ROM + 1
					while ROM_L1 == ROM_L2:
						text1 = "LOADING ..."
						text2 = font.render(text1, True, pygame.Color("white"))
						fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
						CPT_UP = CPT_UP + 1
						if CPT_UP + CPT > MAX:
							CPT = 0
						ROM_L1 = li[CPT_UP + CPT][0][0]
					CPT = CPT + CPT_UP
					affiche()
				#jeux a droite
				if event.key == K_RIGHT:
					CPT = CPT + 1
					affiche()
				#jeux alphabetique -1
				if event.key == K_DOWN:
					ROM_L1 = li[CPT][0][0]
					ROM_L2 = ROM_L1
					CPT_UP=0
					# Tant que la premiere lettre de la ROM est la meme que la premiere lettre de la ROM + 1
					while ROM_L1 == ROM_L2:
						text1 = "LOADING ..."
						text2 = font.render(text1, True, pygame.Color("white"))
						fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
						CPT_UP = CPT_UP - 1
						if CPT_UP + CPT <= NMAX:
							CPT = 0
						ROM_L1 = li[CPT_UP + CPT][0][0]
					CPT = CPT - CPT_UP
<<<<<<< HEAD
=======
					affiche()
>>>>>>> 64e4282477604e8659d766818bcd2a6d352f8da7
				if event.type == QUIT:
					continuer = 0
				if event.key == K_ESCAPE:
					exit()
				# Lancement du script associe dans ${HOME}/BIN/[emulateur].sh $ROM
				# ex : li[CPT][0] = MAME li[CPT][0] = 1942
				# --> /home/[USER]/PYRHARCKADE/BIN/MAME.sh 1942
				if event.key == K_SPACE:
					APP="BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  + " &"
					p = subprocess.Popen(APP, shell=True)
					p.wait()
#					os.system("BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  + " &" )
					
			# Verification pour boucle infinie (wheel)
				#last_update = pygame.time.get_ticks()
			if CPT <= NMAX:
				CPT = 0
			if CPT > MAX:
				CPT = 0
		affiche()


<<<<<<< HEAD
=======

>>>>>>> 64e4282477604e8659d766818bcd2a6d352f8da7

	    
