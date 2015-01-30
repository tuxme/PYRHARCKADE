if MENU_IN == 1:
				if JOY_TEST == 1:

#DEPLACEMENT JOYSTICK
					if event.type == JOYBUTTONDOWN and event.button == 3:

						if (os.path.isfile(IMG + EMU_CHOSE + ".png")):
							BACKGROUNG = IMG + EMU_CHOSE + ".png"
						else:
							BACKGROUNG = BACKGROUNG_ORIG


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
						EMU_CHOSE=str(emu[CPT_EMU])
						if (os.path.isfile(IMG + EMU_CHOSE + ".png")):
							BACKGROUNG = IMG + EMU_CHOSE + ".png"
						else:
							BACKGROUNG = BACKGROUNG_ORIG
						MENU_IN = 0
						fenetre.blit(pygame.transform.scale(pygame.image.load(BACKGROUNG).convert(),(SCREEN_W,SCREEN_H)),(0,0))
						CPT = 0
						# Premier jeu de l emu choisi
						while (str(li[CPT][1]) != EMU_CHOSE):
							CPT = CPT + 1
