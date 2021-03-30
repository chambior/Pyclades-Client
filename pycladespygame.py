import pygame
import inputbox
import network
import board as brd
import godboard

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 18)

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pyclades')

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
	client_live = True
	prevID = -1

	#Déclaration des éléments de l'interface
	commandline = inputbox.InputBox(6, 692, 242, 22, '', COLOR_ACTIVE, COLOR_INACTIVE, FONT)
	board = brd.Board(screen, eval(network.send("getBoard")), [255,6], [1019,708])
	god_board = godboard.GodBoard(screen, eval(network.send("getGods")), eval(network.send("getAuctions")))

	while client_live:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				client_live = False
			command = commandline.handle_event(event)

		#Le vrai programme est ici
		if command != '' and type(command) == str and getID(command) != prevID:
			print(getMsg(command))
			prevID = getID(command)

		#Mettre toute les updates
		commandline.update()
		board.update(eval(network.send("getBoard")))
		getgods = eval(network.send("getGods"))
		#print(getgods)
		god_board.update(getgods, eval(network.send("getAuctions")))

		#Mettre tout les draws
		screen.fill((50, 50, 50))
		commandline.draw(screen)
		board.draw()
		god_board.draw()

		#Laisser à la fin
		pygame.display.flip()
		clock.tick(30)


main()
pygame.quit()
