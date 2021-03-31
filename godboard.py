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
        self.screen = screen
        self.lastplayer = 0
        self.lastvalue = 0
        self.currentplayer = 0
        self.currentvalue = 0
        if(pos!=None):
            self.pos = pos
        else:
            self.pos = 0
        self.rect = pygame.Rect(260, 250+95*self.pos, 270, 90)

    def update(self, pos, auctions):
        #print("AVANT UPDATE {}\n{}\n{}\n{}\n{}".format(self.name, auctions, self.currentplayer, self.currentvalue, self.lastplayer))
        if(pos!=None):
            self.pos = pos
        else:
            self.pos = 0
        if(auctions[0] != self.currentplayer):
            self.lastvalue = self.currentvalue
            self.lastplayer = self.currentplayer
            self.currentplayer = auctions[0]
            self.currentvalue = auctions[1]
        self.rect = pygame.Rect(260, 250+95*self.pos, 270, 90)
        #print("APRES UPDATE {}\n{}\n{}\n{}\n{}".format(self.name, auctions, self.currentplayer, self.currentvalue, self.lastplayer))

    def draw(self):
        #pygame.draw.rect(self.screen, pygame.Color("blue"), self.rect, 2)
        #print("Place : {} Nom : {}".format(self.pos, self.name))
        #print("DRAW Pas d'auctions ici\n{}\n{}\n{}\n{}".format(self.name, self.currentplayer, self.currentvalue, self.lastplayer))
        self.screen.blit(textures.getImage('gods', self.name), [self.rect.x, self.rect.y])
        if(self.lastplayer):
            self.screen.blit(textures.getImage('gods', 'mark_{}'.format(self.lastplayer)),[self.rect.x+8+21*self.lastvalue, self.rect.y+60])
        if(self.currentplayer):
            #print("Params de getimage :\n{}\n{}".format('gods', 'mark_{}'.format(self.currentplayer)))
            self.screen.blit(textures.getImage('gods', 'mark_{}'.format(self.currentplayer)),[self.rect.x+8+21*self.currentplayer, self.rect.y+60])
class GodBoard:
    def __init__(self, screen, gods, auctions):
        self.screen = screen
        self.gods = []
        #             Place d'ares , Place de popo, Place de Athe, Place de zeux
        self.order = [find(1, gods), find(2, gods), find(3, gods), find(4, gods)]

        self.gods.append(God(screen, 'ares'    , self.order[0]))
        self.gods.append(God(screen, 'poseidon', self.order[1]))
        self.gods.append(God(screen, 'athena'  , self.order[2]))
        self.gods.append(God(screen, 'zeus'    , self.order[3]))
        self.gods.append(God(screen, 'appolon', 4))
        self.update(gods, auctions)
        #self.rect = pygame.Rect(255, 245, 280, 469)

    def update(self, gods, auctions):
        self.order = [find(1, gods), find(2, gods), find(3, gods), find(4, gods)]
        for i in range(4):
            self.gods[i].update(self.order[i], auctions[i])
        self.gods[4].update(4, (0,0,0))

    def draw(self):
        for god in self.gods:
            god.draw()
        #pygame.draw.rect(self.screen, pygame.Color("white"), self.rect, 2)
        self.screen.blit(textures.getImage('overlays','gods'), [255,5])
