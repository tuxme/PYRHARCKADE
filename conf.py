def conf_theme (argument2):
	print "-------------"
	print argument2 
	print "-------------"
	
	global BACKGROUNG
	global BACKGROUNG_EMU
	global BACKGROUNG_START
	global BIN_PATH
	global BLACK
	global conf_theme
	global DOCS
	global fenetre
	global font
	global font_path
	global font_size
	global IMG
	global IMG_EMU
	global max_carac
	global MAX_EMU
	global ROMS
	global ROOT_HOME
	global SCREEN_H
	global SCREEN_W
	global SEPARATION_WHEEL_SNAP
	global SIZE_BIN_1
	global SIZE_BIN_2
	global SIZE_BIN_3
	global SIZE_BIN_X_1
	global SIZE_BIN_X_2
	global SIZE_BIN_X_3
	global SIZE_BIN_Y_1
	global SIZE_BIN_Y_2
	global SIZE_BIN_Y_3
	global SIZE_SNAP_CONVERT
	global SIZE_SNAP_CONVERT_H
	global SIZE_SNAP_CONVERT_W
	global SIZE_TEXTE
	global SIZE_TEXTE_H
	global SIZE_TEXTE_W
	global SIZE_WHEEL_CONVERT
	global SIZE_WHEEL_CONVERT_H
	global SIZE_WHEEL_CONVERT_W
	global SLEEP_BEFORE_START
	global SNAP
	global SNAP_AND_WHEEL
	global SOUND
	global WHEEL
	global WHERE_BIN_1
	global WHERE_BIN_1_X
	global WHERE_BIN_1_Y
	global WHERE_BIN_2
	global WHERE_BIN_2_X
	global WHERE_BIN_2_Y
	global WHERE_BIN_3
	global WHERE_BIN_3_X
	global WHERE_BIN_3_Y
	global WHERE_SNAP
	global WHERE_SNAP_X
	global WHERE_SNAP_Y
	global WHERE_TEXTE
	global WHERE_TEXTE_X
	global WHERE_TEXTE_Y
	global WHERE_WHEEL
	global WHERE_WHEEL_X
	global WHERE_WHEEL_Y




	if argument2 == "Y":

	###############################################################1
	###############################################################1
	#		CONFIG FE MODE HORIZONTAL
	###############################################################1
	###############################################################1

		##CONFIG ###############################################

		ROOT_HOME=(os.environ['HOME'] + "/PYRHARCKADE")
		BIN_PATH=(ROOT_HOME + "/BIN/")
		WHEEL=(ROOT_HOME + "/MEDIA/WHEEL/")
		SNAP_AND_WHEEL=(ROOT_HOME + "/MEDIA/")
		SNAP=(ROOT_HOME + "/MEDIA/SNAP/")
		SOUND=(ROOT_HOME + "/MEDIA/SOUND/")
		ROMS=(ROOT_HOME + "/MEDIA/ROMS/")
		DOCS=(ROOT_HOME + "/MEDIA/DOCS/")
		IMG=(ROOT_HOME + "/MEDIA/IMG/")
		BACKGROUNG=(ROOT_HOME + "/MEDIA/IMG/bg2_Y.png")
		BACKGROUNG_EMU=(ROOT_HOME + "/MEDIA/IMG/menu.png")
		IMG_EMU = (ROOT_HOME + "/MEDIA/IMG/EMU/")
		BACKGROUNG_START=(ROOT_HOME + "/MEDIA/IMG/dpfe_welcom.png")
		font_path = "./MEDIA/font.ttf"
		font_size = 20
		max_carac = 20
		font = pygame.font.Font(font_path, font_size)
		BLACK = (ROOT_HOME + "/MEDIA/IMG/black.png")
		SLEEP_BEFORE_START = 4


		##TEMPLATE ##############################################

#		SCREEN_W = root.winfo_screenwidth()
#		SCREEN_H = root.winfo_screenheight()


		SCREEN_W = root.winfo_screenwidth()
		SCREEN_H = root.winfo_screenheight()
		SIZE_SNAP_CONVERT_W = int(floor(SCREEN_W / 3))
		SIZE_SNAP_CONVERT_H = int(floor(SCREEN_H / 5))
		SIZE_SNAP_CONVERT=(SIZE_SNAP_CONVERT_W,SIZE_SNAP_CONVERT_H)
		SIZE_WHEEL_CONVERT_W = SIZE_SNAP_CONVERT_W
		SIZE_WHEEL_CONVERT_H = int(floor(SIZE_WHEEL_CONVERT_W / 4))
		SIZE_WHEEL_CONVERT=(SIZE_WHEEL_CONVERT_W,SIZE_WHEEL_CONVERT_H)
		SEPARATION_WHEEL_SNAP = 10
		WHERE_WHEEL_X = SIZE_WHEEL_CONVERT_W
		WHERE_WHEEL_Y = int(floor(SCREEN_H / 10))
		WHERE_WHEEL=(WHERE_WHEEL_X,WHERE_WHEEL_Y)
		WHERE_SNAP_X = SIZE_WHEEL_CONVERT_W
		WHERE_SNAP_Y = WHERE_WHEEL_Y + SIZE_WHEEL_CONVERT_H + SEPARATION_WHEEL_SNAP
		WHERE_SNAP=(WHERE_SNAP_X,WHERE_SNAP_Y)
		WHERE_TEXTE_X = WHERE_WHEEL_X
		WHERE_TEXTE_Y = int(floor(SCREEN_H / 2))
		SIZE_TEXTE_W = SIZE_SNAP_CONVERT_W
		SIZE_TEXTE_H = int(floor(SIZE_SNAP_CONVERT_H))
		SIZE_TEXTE = (SIZE_TEXTE_W,SIZE_TEXTE_H)
		WHERE_TEXTE=(WHERE_TEXTE_X,WHERE_TEXTE_Y)
		MAX_EMU = 0
		CADRE_W = SIZE_SNAP_CONVERT_W 
		CADRE_H = SIZE_SNAP_CONVERT_H + SIZE_WHEEL_CONVERT_H
		print CADRE_W
		print CADRE_H

		## TAILLE DES MENU EMU

		SIZE_BIN_X_1 = int(floor(SCREEN_W /4))
		SIZE_BIN_Y_1 = SIZE_BIN_X_1
		SIZE_BIN_1 = (SIZE_BIN_X_1,SIZE_BIN_Y_1)

		SIZE_BIN_X_2 = SIZE_BIN_X_1
		SIZE_BIN_Y_2 = SIZE_BIN_X_2
		SIZE_BIN_2 = (SIZE_BIN_X_2,SIZE_BIN_Y_2)

		SIZE_BIN_X_3 = SIZE_BIN_X_2
		SIZE_BIN_Y_3 = SIZE_BIN_X_3
		SIZE_BIN_3 = (SIZE_BIN_X_3,SIZE_BIN_Y_3)

		##EMU CENTRE POSITION

		WHERE_BIN_1_X=int(floor((SCREEN_W / 2)-(SIZE_BIN_X_1/2)))
		WHERE_BIN_1_Y=int(floor((SCREEN_H / 2) - (SIZE_BIN_X_1/2)))
		WHERE_BIN_1=(WHERE_BIN_1_X,WHERE_BIN_1_Y)

		##EMU GAUCHE POSITION

		WHERE_BIN_2_X=WHERE_BIN_1_X
		WHERE_BIN_2_Y=WHERE_BIN_1_Y - (SIZE_BIN_X_1*2)
		WHERE_BIN_2=(WHERE_BIN_2_X,WHERE_BIN_2_Y)

		##EMU GAUCHE POSITION

		WHERE_BIN_3_X=WHERE_BIN_1_X
		WHERE_BIN_3_Y=WHERE_BIN_1_Y + (SIZE_BIN_X_1*2)
		WHERE_BIN_3=(WHERE_BIN_3_X,WHERE_BIN_3_Y)

		##FENETRE PRINCIPAL
		fenetre = [SCREEN_W, SCREEN_H]
		fenetre = pygame.display.set_mode((fenetre),FULLSCREEN)
#		fenetre = pygame.display.set_mode((fenetre)FULLSCREEN)
		#fenetre = pygame.transform.rotate(fenetre, 90)
		#fenetre = pygame.display.set_mode((fenetre))
		fenetre.blit(pygame.transform.scale(pygame.image.load(IMG + "/bg2_Y.png").convert(),(SCREEN_W,SCREEN_H)),(0,0))


	if argument2 == "X":
	###############################################################1
	###############################################################1
	#		CONFIG FE MODE VERTICAL
	###############################################################1
	###############################################################1

		##CONFIG ###############################################

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
		SLEEP_BEFORE_START = 4


		##TEMPLATE ##############################################

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
		SIZE_TEXTE_W = int(floor(SIZE_SNAP_CONVERT_W * 2.5))
		SIZE_TEXTE_H = int(floor(SIZE_SNAP_CONVERT_H))
		SIZE_TEXTE = (SIZE_TEXTE_W,SIZE_TEXTE_H)
		WHERE_TEXTE=(WHERE_TEXTE_X,WHERE_TEXTE_Y)
		MAX_EMU = 0

		## TAILLE DES MENU EMU

		SIZE_BIN_X_1 = int(floor(SCREEN_W /4))
		SIZE_BIN_Y_1 = SIZE_BIN_X_1
		SIZE_BIN_1 = (SIZE_BIN_X_1,SIZE_BIN_Y_1)

		SIZE_BIN_X_2 = SIZE_BIN_X_1*2/3
		SIZE_BIN_Y_2 = SIZE_BIN_X_2
		SIZE_BIN_2 = (SIZE_BIN_X_2,SIZE_BIN_Y_2)

		SIZE_BIN_X_3 = SIZE_BIN_X_2
		SIZE_BIN_Y_3 = SIZE_BIN_X_3
		SIZE_BIN_3 = (SIZE_BIN_X_3,SIZE_BIN_Y_3)

		##EMU CENTRE POSITION

		WHERE_BIN_1_X=int(floor((SCREEN_W / 2)-(SIZE_BIN_X_1/2)))
		WHERE_BIN_1_Y=int(floor((SCREEN_H / 2) - (SIZE_BIN_X_1/2)))
		WHERE_BIN_1=(WHERE_BIN_1_X,WHERE_BIN_1_Y)

		##EMU GAUCHE POSITION

		WHERE_BIN_2_X=int(floor((SCREEN_W / 3)-(SIZE_BIN_X_2/2)))
		WHERE_BIN_2_Y=int(floor(SCREEN_H / 2))
		WHERE_BIN_2=(WHERE_BIN_2_X,WHERE_BIN_2_Y)

		##EMU GAUCHE POSITION

		WHERE_BIN_3_X=int(floor((SCREEN_W * 2 / 3)-(SIZE_BIN_X_3/2)))
		WHERE_BIN_3_Y=int(floor(SCREEN_H / 2))
		WHERE_BIN_3=(WHERE_BIN_3_X,WHERE_BIN_3_Y)

		##FENETRE PRINCIPAL
		fenetre = [SCREEN_W, SCREEN_H]
		fenetre = pygame.display.set_mode((fenetre),FULLSCREEN)
		#fenetre = pygame.display.set_mode((fenetre))
		fenetre.blit(pygame.transform.scale(pygame.image.load(IMG + "/bg2.png").convert(),(SCREEN_W,SCREEN_H)),(0,0))


