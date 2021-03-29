import pygame
import os

images = {}
dirs = os.listdir("assets/textures")

for dir in dirs:
    files = os.listdir("assets/textures/{}".format(dir))
    for file in files:
        if file[-4:] == '.png':
            try:
                images[dir][file[:-4]] = pygame.image.load("./assets/textures/{}/{}".format(dir, file))
            except KeyError:
                images[dir] = {}
                images[dir][file[:-4]] = pygame.image.load("./assets/textures/{}/{}".format(dir, file))

def getImage(category, image):
    return images[category][image];
