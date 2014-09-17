#!/usr/bin/env python
#-*- coding: utf-8 -*-
# PYRHARCKADE is a simple pygame front for PIMAME
# version: 1.8.B
# guillaume@tuxme.net
# GPL Licence

import pygame
from Tkinter import*
import time
import csv
import os
import sys
import subprocess
from pygame.locals import *
from pygame.compat import unicode_

from math import *
clock = pygame.time.Clock()

root = Tk()
pygame.init()
total = len(sys.argv)
print total
if total == 1:
	argument1 = "YES"
	argument2 = "X"
if total == 2:
	argument1 = str(sys.argv[1])
	argument2 = "X"
if total == 3:
	argument1 = str(sys.argv[1])
	argument2 = str(sys.argv[2])


execfile("./conf.py")
conf_theme(argument2)


#COMPTEUR et lecture du fichier conf 

CPT = 0
CPT_EMU = 0
MAX = 0
MAX_EMU = 0

#COMPTEUR et lecture du fichier conf
reader = csv.reader(file(ROOT_HOME + "/ROM_CONFIG_FILES.csv" ))
li = []
emu = []

for row in reader:
        li.append(row)
	if not (li[MAX][1] in emu):
		emu.append(li[MAX][1])
		MAX_EMU=MAX_EMU +1
	MAX = MAX +1

#Remise a 0 en start
MAX = MAX - 1
NMAX=(MAX * -1)
MAX_EMU = MAX_EMU - 1
NMAX_EMU = (MAX_EMU  * -1) 
li = sorted(li)
emu = sorted(emu)

#Variable utilisé pour lancement menu emu et 1 er jeux
AFFICHE_EMU_START=1
AFFICHE_GAME_START=1
FIRST=1
FIRST_VID=1
#Gestion time out video 

T1 = time.time()
T2 = time.time()

# Test lancement First ou lancement auto suite fin emu
continuer = 1
MENU_IN=1
MENU_GO=1

if MAX_EMU==0:
	MENU_IN=0
	EMU_CHOSE=emu[0]

################################### Initialisation son
pygame.mixer.init()

intro_sound = pygame.mixer.Sound(SOUND + "intro.wav")

#time.sleep(5)

# Initialisation / ou non du joystick 0
if pygame.joystick.get_count() != 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init()
	JOY_TEST = 1
	print "----- Joy OK"
else:
	JOY_TEST = 0


###################################################################
#		AFFICHAGE MENU EMULATEUR
###################################################################
			

def affiche_menu():
	if MAX_EMU==1:
		if (CPT_EMU+1) > MAX_EMU:
			IMG_EMU_PATH_D=IMG_EMU + emu[CPT_EMU-1] +".png"
		else:
			IMG_EMU_PATH_D=IMG_EMU + emu[CPT_EMU+1] +".png"
		IMG_EMU_PATH_G=IMG_EMU_PATH_D
	else:
		if (CPT_EMU+1) > MAX_EMU:
			IMG_EMU_PATH_D=IMG_EMU + emu[NMAX_EMU] +".png"
			IMG_EMU_PATH_G=IMG_EMU + emu[CPT_EMU-1] +".png"
		else:
			IMG_EMU_PATH_D=IMG_EMU + emu[CPT_EMU+1] +".png"
			IMG_EMU_PATH_G=IMG_EMU + emu[CPT_EMU-1] +".png"

	IMG_EMU_PATH=IMG_EMU + emu[CPT_EMU] +".png"
	fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_EMU_PATH_D).convert(),(SIZE_BIN_2)),(WHERE_BIN_2))
	fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_EMU_PATH_G).convert(),(SIZE_BIN_2)),(WHERE_BIN_3))
	fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_EMU_PATH).convert(),(SIZE_BIN_1)),(WHERE_BIN_1))

###################################################################
#		AFFICHAGE MENU JEUX
###################################################################
def affiche(FIRST_VID):

	IMG_WHEEL=SNAP_AND_WHEEL  +EMU_CHOSE+"/WHEEL/"+li[CPT][0]+".png"
	IMG_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/SNAP/"+li[CPT][0]+".png"
	FILE_INFO = SNAP_AND_WHEEL +EMU_CHOSE+"/DOCS/"+ li[CPT][0] + ".txt"
	VIDEO_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/VIDEO/"+li[CPT][0]+".mpg"
	if os.path.isfile(FILE_INFO):
		FILE_DOC = open(FILE_INFO,"r")
		text1 = FILE_DOC.read()
		LPLUS=0
		LPLUS=LPLUS + (font_size+5)
		WHERE_TEXTE=(WHERE_TEXTE_X,WHERE_TEXTE_Y)
		fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_TEXTE)),(WHERE_TEXTE))
		for ligne in text1.splitlines():
			ligne=ligne[0:max_carac]
			x,y = fenetre.blit(font.render(ligne,5,pygame.Color("white")),(WHERE_TEXTE_X,WHERE_TEXTE_Y+LPLUS)).bottomleft
			LPLUS=LPLUS + (font_size+5)
		FILE_DOC.close()
	else:
		text1 = "No DATA File : " + li[CPT][0] 
		text2 = font.render(text1, True, pygame.Color("white"))
		fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_TEXTE_W,SIZE_TEXTE_H)),((WHERE_TEXTE_X,WHERE_TEXTE_Y)))
		fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y+50)).bottomleft
	if not (os.path.isfile(IMG_WHEEL)):
		IMG_WHEEL = SNAP_AND_WHEEL + "no_wheel.png"
	if not (os.path.isfile(IMG_SNAP)):
		IMG_SNAP = SNAP_AND_WHEEL + "no_snap.png"

		
	fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_WHEEL_CONVERT)),(WHERE_WHEEL))
	fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))
	fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_WHEEL).convert_alpha(),(SIZE_WHEEL_CONVERT)),(WHERE_WHEEL))
	fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_SNAP).convert(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))

	global T2
	if T2 == 0:
		T2 = time.time()
		return T2

	VIDEO_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/VIDEO/"+li[CPT][0]+".mpg"

	if (os.path.isfile(VIDEO_SNAP)):
		play_video(FIRST_VID)
###################################################################
#		AFFICHAGE VIDEO JEUX
###################################################################
def play_video(X):
	pygame.mixer.quit()
	FIRST_VID=X
	if FIRST_VID == 1:
		FIRST_VID = 0
		global FIRST_VID
	else :	
		pygame.mixer.quit()
#		pygame.mixer.init()
		if T2 != 0:
			T2 = time.time()
		IMG_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/SNAP/"+li[CPT][0]+".png"
		VIDEO_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/VIDEO/"+li[CPT][0]+".mpg"
		fenetre.blit(pygame.transform.scale(pygame.image.load(IMG_SNAP).convert(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))
		elapsed = T2 - T1
		if elapsed > 3 and os.path.isfile(VIDEO_SNAP) :
			fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))
			global T2
			global T1
			FPS = 60

			movie = pygame.movie.Movie(VIDEO_SNAP)
			movie.set_volume(0.8)
			mrect = pygame.Rect(WHERE_SNAP_X,WHERE_SNAP_Y,SIZE_SNAP_CONVERT_W,SIZE_SNAP_CONVERT_H)
			movie.set_display(fenetre,mrect)

			fenetre.blit(pygame.transform.scale(pygame.image.load(BLACK).convert(),(SIZE_SNAP_CONVERT)),(WHERE_SNAP))
			movie.play()
	#		pygame.time.set_timer(USEREVENT, 10000)
			while movie.get_busy():
				evt = pygame.event.wait()
				if evt.type == QUIT:
					T2=0
					T1=time.time()
					return T2
					return T1
					movie.stop()
					break
				if evt.type == KEYDOWN:
					movie.stop()
					T2=0
					T1=time.time()
					return T1
					return T2
					break



#MAIN #################################################
pygame.key.set_repeat(400, 50)
PLAY_SNAP=True
while continuer:
# PREMIER LANCEMENT (y/n) SI YES passe ecran d'acceuil
	if FIRST == 1:

		if argument1 == "YES":
			FIRST=0
		else:
# AFFICHAGE ECRAN ACCEUIL
			intro_sound.play()
			fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_START).convert(),(SCREEN_W,SCREEN_H)),(0,0))
			
			pygame.display.update()
			FIRST = 0
			time.sleep(SLEEP_BEFORE_START)
	else:

# RESTE AFFICHAGE ####################################
		if MENU_IN == 1:
			if AFFICHE_EMU_START == 1:
				fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_EMU).convert(),(SCREEN_W,SCREEN_H)),(0,0))
				AFFICHE_EMU_START = 0
			pygame.display.update()
			affiche_menu()
		if MENU_IN == 0:
			if AFFICHE_GAME_START == 1:
				CPT = 0
				CPT_UP = 0
				# Premier jeu de l emu choisi
				while (str(li[CPT][1]) != EMU_CHOSE):
					CPT = CPT + 1

				fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG).convert(),(SCREEN_W,SCREEN_H)),(0,0))
				AFFICHE_GAME_START = 0
			if MENU_GO == 1:
				CPT = 0
				CPT_UP = 0
				# Premier jeu de l emu choisi
				while (str(li[CPT][1]) != EMU_CHOSE):
					CPT = CPT + 1
				MENU_GO = 0
			pygame.display.update()
			affiche(FIRST_VID)
		for event in pygame.event.get():

###################################################################
#		DEPLACEMENT MENU JEUX
###################################################################
			if MENU_IN == 0:
#		DEPLACEMENT JOYSTICK
###################################################################
				if JOY_TEST == 1:
					execfile("./move_input_joystick.py")
###################################################################
#		DEPLACEMENT CLAVIER
###################################################################
				if event.type == KEYDOWN:
					execfile("./move_input_keyboard.py")
					print "---------------------------"
###################################################################
#		DEPLACEMENT MENU EMULATEUR
###################################################################
			execfile("./move_input.py")
###################################################################
#		COMPTEUR MAX / MIN Pour exception
###################################################################			
			CPT_TMP=CPT	
			if CPT < NMAX:
				CPT = 0 
                                while (str(li[CPT][1]) != EMU_CHOSE):
                                        CPT = CPT + 1
				print "NMAX"

			if CPT > MAX:
				CPT = 0 
                                while (str(li[CPT][1]) != EMU_CHOSE):
                                        CPT = CPT + 1
				print "MAX"

#			NMAX_EMU_TMP=NMAX_EMU - 1 
#			MAX_EMU_TMP=NMAX_EMU - 1 
			if MAX_EMU==0:
				if CPT_EMU < NMAX_EMU:
					CPT_EMU = 0
				if CPT_EMU >= MAX_EMU:
					CPT_EMU = 0
			else:
				if CPT_EMU < NMAX_EMU:
					CPT_EMU = 0 
				if CPT_EMU > MAX_EMU:
					#CPT_EMU = NMAX_EMU
					CPT_EMU = 0

			if MAX_EMU == 0:
				CPT_EMU=0
			print " => CPT:" + str(CPT) + " | NMAX:" + str(NMAX) + " | MAX:" + str(MAX) + " | CPT_EMU:" + str(CPT_EMU) + " NMAX_EMU:" + str(NMAX_EMU) + " MAX_EMU:" + str(MAX_EMU) + "     >> " + li[CPT][0]


