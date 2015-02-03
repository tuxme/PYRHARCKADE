
#--------------------------------------- LANCEMENT JEUX AVEC EMU
if event.type == JOYBUTTONDOWN and event.button == 3:
	APP="BIN/" + li[CPT][1] +".sh" + " " + li[CPT][0] + " " + Orientation 
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
		affiche(FIRST_VID)
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
				CPT = 0
				while (str(li[CPT][1]) != EMU_CHOSE):
					CPT = CPT + 1
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
				CPT = 0
				while (str(li[CPT][1]) != EMU_CHOSE):
					CPT = CPT + 1
				break
			ROM_L1 = li[CPT][0][0]

#--------------------------------------- SELECTION JEUX A DROITE (+1)
	if event.axis == 0 and event.value > 0:
		if CPT + 1 > MAX:
			CPT = 0
			while (str(li[CPT][1]) != EMU_CHOSE):
				CPT = CPT + 1
		else:
			CPT= CPT + 1
			while str(li[CPT][1]) != EMU_CHOSE:
				text1 = "LOADING ..."
				text2 = font.render(text1, True, pygame.Color("white"))
				fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
				CPT = CPT + 1
				if CPT > MAX:
					CPT = 0
			#		break
#--------------------------------------- SELECTION JEUX A GAUCHE (-1)
	if event.axis == 0 and event.value < 0:
		if CPT < NMAX:
			CPT = 0
			while (str(li[CPT][1]) != EMU_CHOSE):
				CPT = CPT + 1
		else:
			CPT= CPT - 1
			while str(li[CPT][1]) != EMU_CHOSE:
				text1 = "LOADING ..."
				text2 = font.render(text1, True, pygame.Color("white"))
				fenetre.blit(text2,(WHERE_TEXTE_X,WHERE_TEXTE_Y)).bottomleft
				CPT = CPT - 1
				if CPT < NMAX:
					CPT = 0
			#		break
