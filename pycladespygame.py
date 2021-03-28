import pygame
import inputbox
import network
import board as brd

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 18)

screen = pygame.display.set_mode((1280, 720))

def getID(str):
	i = 0
	while str[i] in '0123456789':
		i+=1
	return str[:i]

def getMsg(str):
	i = 0
	while str[i] in '0123456789':
		i+=1
	return str[i+1:]


def main():
	clock = pygame.time.Clock()
	client_live = False
	prevID = -1

	#Déclaration des éléments de l'interface
	commandline = inputbox.InputBox(6, 692, 242, 22, '', COLOR_ACTIVE, COLOR_INACTIVE, FONT)
	board = brd.Board(screen, [255,6], [1019,708])

	while not client_live:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				client_live = True
			command = commandline.handle_event(event)

		#Le vrai programme est ici
		if command != '' and type(command) == str and getID(command) != prevID:
			print(getMsg(command))
			prevID = getID(command)

		#Mettre toute les updates
		commandline.update()
		board.update(network.send("getBoard"))

		#Mettre tout les draws
		screen.fill((50, 50, 50))
		commandline.draw(screen)
		board.draw()

		#Laisser à la fin
		pygame.display.flip()
		clock.tick(30)


main()
pygame.quit()
