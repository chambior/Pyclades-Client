
pygame.font.init()

def size(x, y):
	global screen
	global stroke_value
	global fill_value
	screen = pygame.display.set_mode((x, y))
	color = [0,0,0]
	stroke_value = 0

def background(r,g,b):
	global screen
	screen.fill((r,g,b))

def noStroke():
	global stroke_value
	stroke_value = 0

def stroke(x):
	global stroke_value
	stroke_value = x

def fill(x):
	global fill_value
	fill_value = x

def text(str, x, y):
	myfont = pygame.font.SysFont('Arial', 12)
	textsurface = myfont.render(str, False, (0, 0, 0))
	screen.blit(textsurface,(x,y))

def mouseX():
	return pygame.mouse.get_pos()[0]

def mouseY():
	return pygame.mouse.get_pos()[1]

def rect(x,y,sx,sy):
	global screen
	global fill_value
	rect = Rect(x,y, sx, sy)
	pygame.draw.rect(screen, (fill_value, fill_value, fill_value), rect)

def mousePressed():
	return pygame.mouse.get_pressed()

def keyPressed():
	_keys = pygame.key.get_focused()
	for _key in "azertyuiopqsdfghjklmwxcvbn1234567890":
		_key_code = pygame.key.key_code(_key)
		if _keys[_key_code]:
			return _key

def key():
	print(pygame.key.get_pressed())
	return 'a'


def line(x1, y1, x2, y2):
	global screen
	global stroke_value

	color = (fill_value, fill_value, fill_value)
	start_pos = (x1, y1)
	end_pos = (x2, y2)
	pygame.draw.line(screen, color, start_pos, end_pos, stroke_value)

setup()
while(1):
	draw()
	pygame.display.flip()
