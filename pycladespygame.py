import pygame
import inputbox

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 16)

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
	commandline = inputbox.InputBox(100, 500, 280, 16, '', COLOR_ACTIVE, COLOR_INACTIVE, FONT)
	client_live = False
	prevID = -1
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

		#Mettre tout les draws
		screen.fill((255, 255, 255))
		commandline.draw(screen)

		#Laisser à la fin
		pygame.display.flip()
		clock.tick(30)


main()
pygame.quit()
