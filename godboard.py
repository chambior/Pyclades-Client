import pygame
import textures

#retourne l'indice de l'élément e dans le tableau a
def find(e,a):
    for i in range(len(a)):
        if(a[i] == e):
            return i


class God:
    def __init__(self, screen, name, pos):
        self.name = name
        self.lastplayer = 0
        self.lastvalue = 0
        self.currentplayer = 0
        self.currentvalue = 0
        self.pos = pos

    def update(self, pos, auctions):
        self.pos = pos
        if(auctions[0] != self.currentplayer):
            self.lastvalue = self.currentvalue
            self.lastplayer = self.currentplayer
            self.currentplayer = auctions[0]
            self.currentvalue = auctions[1]

    def draw(self):
        pass

class GodBoard:
    def __init__(self, screen, gods, auctions):
        self.screen = screen
        self.gods = []
        #             Place d'ares , Place de popo, Place de Athe, Place de zeux
        self.order = [find(1, gods), find(2, gods), find(3, gods), find(4, gods)]
        for god in gods:
            self.gods.append(God(screen, 'ares'    , self.order[0]))
            self.gods.append(God(screen, 'poseidon', self.order[1]))
            self.gods.append(God(screen, 'athena'  , self.order[2]))
            self.gods.append(God(screen, 'zeus'    , self.order[3]))
        self.update(gods, auctions)
        self.rect = pygame.Rect(255, 245, 280, 469)

    def update(self, gods, auctions):
        #ranger les dieux (self.order)
        for i in range(4):
            self.gods[i].update(self.order[i], auctions[i])

    def draw(self):
        for god in self.gods:
            god.draw()
        pygame.draw.rect(self.screen, pygame.Color("white"), self.rect, 2)
