#!/usr/bin/env python
#-*- coding: utf-8 -*-

# PYRHARCKADE is a simple pygame front for PIMAME
# version: 0.9a
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

#CONFIG ###############################################

ROOT_HOME=(os.environ['HOME'] + "/PYRHARCKADE")
BIN_PATH=(ROOT_HOME + "/BIN/")
WHEEL=(ROOT_HOME + "/MEDIA/WHEEL/")
SNAP_AND_WHEEL=(ROOT_HOME + "/MEDIA/")
SNAP=(ROOT_HOME + "/MEDIA/SNAP/")
SOUND=(ROOT_HOME + "/MEDIA/SOUND/")
ROMS=(ROOT_HOME + "/MEDIA/ROMS/")
DOCS=(ROOT_HOME + "/MEDIA/DOCS/")
IMG=(ROOT_HOME + "/MEDIA/IMG/")
BACKGROUNG=(ROOT_HOME + "/MEDIA/IMG/bg2.png")
BACKGROUNG_EMU=(ROOT_HOME + "/MEDIA/IMG/menu.png")
IMG_EMU = (ROOT_HOME + "/MEDIA/IMG/EMU/")
BACKGROUNG_START=(ROOT_HOME + "/MEDIA/IMG/dpfe_welcom.png")
font_path = "./MEDIA/font.ttf"
font_size = 30
max_carac = 30
font = pygame.font.Font(font_path, font_size)
BLACK = (ROOT_HOME + "/MEDIA/IMG/black.png")
SLEEP_BEFORE_START = 1

#TEMPLATE ##############################################

SCREEN_W = root.winfo_screenwidth() - 200
SCREEN_H = root.winfo_screenheight() - 200
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
SIZE_TEXTE_W = int(floor(SIZE_SNAP_CONVERT_W * 2.5))
SIZE_TEXTE_H = int(floor(SIZE_SNAP_CONVERT_H))
SIZE_TEXTE = (SIZE_TEXTE_W,SIZE_TEXTE_H)
WHERE_TEXTE=(WHERE_TEXTE_X,WHERE_TEXTE_Y)


# TAILLE DES MENU EMU

SIZE_BIN_X_1 = int(floor(SCREEN_W /4))
SIZE_BIN_Y_1 = SIZE_BIN_X_1
SIZE_BIN_1 = (SIZE_BIN_X_1,SIZE_BIN_Y_1)

SIZE_BIN_X_2 = SIZE_BIN_X_1*2/3
SIZE_BIN_Y_2 = SIZE_BIN_X_2
SIZE_BIN_2 = (SIZE_BIN_X_2,SIZE_BIN_Y_2)

SIZE_BIN_X_3 = SIZE_BIN_X_2
SIZE_BIN_Y_3 = SIZE_BIN_X_3
SIZE_BIN_3 = (SIZE_BIN_X_3,SIZE_BIN_Y_3)

#EMU CENTRE POSITION

WHERE_BIN_1_X=int(floor((SCREEN_W / 2)-(SIZE_BIN_X_1/2)))
WHERE_BIN_1_Y=int(floor((SCREEN_H / 2) - (SIZE_BIN_X_1/2)))
WHERE_BIN_1=(WHERE_BIN_1_X,WHERE_BIN_1_Y)

#EMU GAUCHE POSITION

WHERE_BIN_2_X=int(floor((SCREEN_W / 3)-(SIZE_BIN_X_2/2)))
WHERE_BIN_2_Y=int(floor(SCREEN_H / 2))
WHERE_BIN_2=(WHERE_BIN_2_X,WHERE_BIN_2_Y)

#EMU GAUCHE POSITION

WHERE_BIN_3_X=int(floor((SCREEN_W * 2 / 3)-(SIZE_BIN_X_3/2)))
WHERE_BIN_3_Y=int(floor(SCREEN_H / 2))
WHERE_BIN_3=(WHERE_BIN_3_X,WHERE_BIN_3_Y)


#FENETRE PRINCIPAL 
fenetre = [SCREEN_W, SCREEN_H]
#fenetre = pygame.display.set_mode((fenetre),FULLSCREEN)
fenetre = pygame.display.set_mode((fenetre))
fenetre.blit(pygame.transform.scale(pygame.image.load(IMG + "/bg2.png").convert(),(SCREEN_W,SCREEN_H)),(0,0))


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

#Gestion time out video 

T1 = time.time()
T2 = time.time()

# Test lancement First ou lancement auto suite fin emu
continuer = 1
total = len(sys.argv)
if total > 1:
	argument1 = str(sys.argv[1])

else:
	argument1 = "NO"

MENU_IN=1
MENU_GO=1

if MAX_EMU==0:
	MENU_IN=0
	EMU_CHOSE=emu[0]

################################### Initialisation son
pygame.mixer.init()

intro_sound = pygame.mixer.Sound(SOUND + "intro.wav")

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
def affiche():

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
	play_video()

def play_video():
	if T2 != 0:
		T2 = time.time()
	VIDEO_SNAP=SNAP_AND_WHEEL +EMU_CHOSE+"/VIDEO/"+li[CPT][0]+".mpg"
	elapsed = T2 - T1
	print str(T2)
	print str(T1)
	print elapsed
	print VIDEO_SNAP
	if elapsed > 2 and os.path.isfile(VIDEO_SNAP) :
		global T2
		global T1
		FPS = 60
		movie = pygame.movie.Movie(VIDEO_SNAP)
		mrect = pygame.Rect(WHERE_SNAP_X,WHERE_SNAP_Y,SIZE_SNAP_CONVERT_H,SIZE_SNAP_CONVERT_W)
		movie.set_display(fenetre,mrect)
		movie.set_volume(100)
		movie.play()
		pygame.time.set_timer(USEREVENT, 10000)
		while movie.get_busy():
			evt = pygame.event.wait()
			if evt.type == QUIT:
				print "movie stop"
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
				print "movie stop"
				return T2
				break



#MAIN #################################################
pygame.key.set_repeat(400, 100)
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
			affiche()
		for event in pygame.event.get():

###################################################################
#		DEPLACEMENT MENU JEUX
###################################################################
			if MENU_IN == 0:
#		DEPLACEMENT JOYSTICK
###################################################################
				if JOY_TEST == 1:

#--------------------------------------- LANCEMENT JEUX AVEC EMU
					if event.type == JOYBUTTONDOWN and event.button == 3:
						APP="BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  
						p = subprocess.Popen(APP, shell=True)
						sys.exit("GO play bitch ;)")
#--------------------------------------- RETOUR EMU MENU
					if event.type == JOYBUTTONDOWN and event.button == 1:
						if MAX_EMU==0:
							MENU_IN=0
							EMU_CHOSE=emu[0]
							CPT=0
							while (str(li[CPT][1]) != EMU_CHOSE):
								CPT = CPT + 1
							affiche()
							affiche_menu()

						else:
							fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_EMU).convert(),(SCREEN_W,SCREEN_H)),(0,0))
							MENU_IN = 1
						fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_EMU).convert(),(SCREEN_W,SCREEN_H)),(0,0))

					if event.type == JOYAXISMOTION:
						T1 = time.time()
#--------------------------------------- SELECTION JEUX PAR LETTRE (-1 0-Z)
						if event.axis == 1 and event.value > 0:
							ROM_L1 = li[CPT][0][0]
							ROM_L2 = ROM_L1
							CPT_UP = 0
							while ((ROM_L1 == ROM_L2) | (str(li[CPT][1]) != EMU_CHOSE)):
								text1 = "LOADING ... : "
								text2 = font.render(text1, True, pygame.Color("white"))
								fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
								CPT = CPT - 1
								if CPT < NMAX:
									MENU_GO == 1
									break
								ROM_L1 = li[CPT][0][0]
#--------------------------------------- SELECTION JEUX PAR LETTRE (-1 0-Z)
						if event.axis == 1 and event.value < 0:
							ROM_L1 = li[CPT][0][0]
							ROM_L2 = ROM_L1
							CPT_UP = 0

							while ((ROM_L1 == ROM_L2) | (str(li[CPT][1]) != EMU_CHOSE)):
								text1 = "LOADING ... : "
								text2 = font.render(text1, True, pygame.Color("white"))
								fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
								CPT = CPT + 1
								if CPT > MAX:
									MENU_GO == 1
									break
								ROM_L1 = li[CPT][0][0]

#--------------------------------------- SELECTION JEUX A DROITE (+1)
						if event.axis == 0 and event.value > 0:
							if CPT + 1 > MAX:
								CPT = 0
							else:
								CPT= CPT + 1
								while str(li[CPT][1]) != EMU_CHOSE:
									text1 = "LOADING ..."
									text2 = font.render(text1, True, pygame.Color("white"))
									fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
									CPT = CPT + 1
									if CPT > MAX:
										CPT = 0
										break
#--------------------------------------- SELECTION JEUX A GAUCHE (-1)
						if event.axis == 0 and event.value < 0:
							if CPT < NMAX:
								CPT = 0
							else:
								CPT= CPT - 1
								while str(li[CPT][1]) != EMU_CHOSE:
									text1 = "LOADING ..."
									text2 = font.render(text1, True, pygame.Color("white"))
									fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
									CPT = CPT - 1
									if CPT < NMAX:
										CPT = 0
										break

###################################################################
#		DEPLACEMENT CLAVIER
###################################################################

				if event.type == KEYDOWN:

					T1 = time.time()
					print EMU_CHOSE + " => CPT:" + str(CPT) + "CPT_EMU:" + str(CPT_EMU) + " ... MAX("+ str(MAX) + "),NAMX(" + str(NMAX) + "),MAX_EMU(" + str(MAX_EMU) + "),NMAX_EMU(" + str(NMAX_EMU)  + ")  >> " + li[CPT][0]

#--------------------------------------- SELECTION JEUX A DROITE (+1)
					if event.key == K_RIGHT:

						if CPT + 1 > MAX:
							CPT = 0
						else:
							CPT= CPT + 1
							while str(li[CPT][1]) != EMU_CHOSE:
								text1 = "LOADING ..."
								text2 = font.render(text1, True, pygame.Color("white"))
								fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
								CPT = CPT + 1
								if CPT > MAX:
									CPT = 0
									break
#--------------------------------------- SELECTION JEUX A GAUCHE (-1)
					if event.key == K_LEFT:
						if CPT < NMAX:
							CPT = 0
						else:
							CPT= CPT - 1
							while str(li[CPT][1]) != EMU_CHOSE:
								text1 = "LOADING ..."
								text2 = font.render(text1, True, pygame.Color("white"))
								fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
								CPT = CPT - 1
								if CPT < NMAX:
									CPT = 0
									break
#--------------------------------------- SELECTION JEUX PAR LETTRE (+1 0-Z)
					if event.key == K_UP:
						ROM_L1 = li[CPT][0][0]
						ROM_L2 = ROM_L1
						CPT_UP = 0

						while ((ROM_L1 == ROM_L2) | (str(li[CPT][1]) != EMU_CHOSE)):
							text1 = "LOADING ... : "
							text2 = font.render(text1, True, pygame.Color("white"))
							fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
							CPT = CPT + 1
							if CPT > MAX:
								MENU_GO == 1
								break
							ROM_L1 = li[CPT][0][0]
#--------------------------------------- SELECTION JEUX PAR LETTRE (-1 0-Z)
					if event.key == K_DOWN:
						ROM_L1 = li[CPT][0][0]
						ROM_L2 = ROM_L1
						CPT_UP = 0
						while ((ROM_L1 == ROM_L2) | (str(li[CPT][1]) != EMU_CHOSE)):
							text1 = "LOADING ... : "
							text2 = font.render(text1, True, pygame.Color("white"))
							fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
							CPT = CPT - 1
							if CPT < NMAX:
								MENU_GO == 1
								break
							ROM_L1 = li[CPT][0][0]

#--------------------------------------- LANCEMENT DU JEUX + EXIT FE
					if event.type == QUIT:
						continuer = 0
					if event.key == K_b:
						if MAX_EMU==0:
							MENU_IN=0
							EMU_CHOSE=emu[0]
							CPT=0
							while (str(li[CPT][1]) != EMU_CHOSE):
								CPT = CPT + 1
							affiche()
							affiche_menu()

						else:
							fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_EMU).convert(),(SCREEN_W,SCREEN_H)),(0,0))
							MENU_IN = 1
						fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG_EMU).convert(),(SCREEN_W,SCREEN_H)),(0,0))
					if event.key == K_SPACE:
						print "Launch "+li[CPT][0] + " with " + EMU_CHOSE
						APP="BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0]  
						p = subprocess.Popen(APP, shell=True)
						sys.exit("GO play bitch ;)")
#--------------------------------------- QUIT Si un seul emu
					if (event.key == K_ESCAPE) & (MAX_EMU == 0):
						exit()

###################################################################
#		DEPLACEMENT MENU EMULATEUR
###################################################################
			if MENU_IN == 1:
				if JOY_TEST == 1:

#DEPLACEMENT JOYSTICK
					if event.type == JOYBUTTONDOWN and event.button == 3:
						MENU_IN = 0
						fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG).convert(),(SCREEN_W,SCREEN_H)),(0,0))
						EMU_CHOSE=str(emu[CPT_EMU])
						CPT = 0
						# Premier jeu de l emu choisi
						while (str(li[CPT][1]) != EMU_CHOSE):
							CPT = CPT + 1

					if event.type == JOYAXISMOTION:
#--------------------------------------- SELECTION EMULATEUR A GAUCHE (-1)
						if event.axis == 0 and event.value > 0:
							CPT_EMU = CPT_EMU - 1
#--------------------------------------- SELECTION EMULATEUR A DROITE (+1)
						if event.axis == 0 and event.value < 0:
							CPT_EMU = CPT_EMU + 1


#DEPLACEMENT CLAVIER


				if event.type == KEYDOWN:
#--------------------------------------- SELECTION EMULATEUR A GAUCHE (-1)
					if event.key == K_LEFT:
						CPT_EMU = CPT_EMU + 1
#--------------------------------------- SELECTION EMULATEUR A DROITE (+1)
					if event.key == K_RIGHT:
						CPT_EMU = CPT_EMU - 1
#--------------------------------------- EXIT FE
					if event.type == QUIT:
						continuer = 0
					if event.key == K_ESCAPE:
						exit()
#--------------------------------------- SELECTION EMULATEUR 
					if event.key == K_SPACE:
						MENU_IN = 0
						fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG).convert(),(SCREEN_W,SCREEN_H)),(0,0))
						EMU_CHOSE=str(emu[CPT_EMU])
						CPT = 0
						# Premier jeu de l emu choisi
						while (str(li[CPT][1]) != EMU_CHOSE):
							CPT = CPT + 1



###################################################################
#		COMPTEUR MAX / MIN Pour exception
###################################################################			
				
			if CPT < NMAX:
				CPT = 0
			if CPT > MAX:
				CPT = 0
			if MAX_EMU==0:
				if CPT_EMU < NMAX_EMU:
					CPT_EMU = 0
				if CPT_EMU >= MAX_EMU:
					CPT_EMU = -1
			else:
				if CPT_EMU < NMAX_EMU:
					CPT_EMU = 0
				if CPT_EMU > MAX_EMU:
					CPT_EMU = NMAX_EMU

			if MAX_EMU == 0:
				CPT_EMU=0


