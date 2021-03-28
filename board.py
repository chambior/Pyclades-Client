import pygame

class Board:
    def __init__(self, screen, startcoords = [100,300], startsize = [500,500]):
        self.rect = pygame.Rect(startcoords[0], startcoords[1], startsize[0], startsize[1])
        self.screen = screen
    def update(self, board):
        pass#WIP
    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color("white"), self.rect, 2)
