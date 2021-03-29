import pygame
import textures
import math


def averageCoords(list):
	sum = [0,0]
	for c in list:
		sum[0] += c[0]
		sum[1] += c[1]
	sum[0] = sum[0]/len(list)
	sum[1] = sum[1]/len(list)
	return sum


class Map:
    def __init__(self, surface, tiles, offset = [100,612]):
        self.surface = surface
        self.update(tiles)
        self.offset = [offset[0] + 10, offset[1]]
    def update(self, tiles):
        self.tiles = tiles
    def draw(self):
        xOffset = self.offset[0]
        yOffset = self.offset[1]
        self.surface.blit(textures.getImage('maps', 'map5'), [xOffset-40, yOffset-329])
        #Le code ci-après permet l'affichage de n'importe quelle carte, mais c'est moins joli
        """
        for i in self.tiles:
            ei = eval(i)
            pygame.draw.circle(self.surface, pygame.Color("white"),
                [xOffset + ei[0] * 32 + ei[1] * 32,
                yOffset + ei[0] * 56 - ei[1] * 56],
                33)
        for i in self.tiles:
            ei = eval(i)
            if(self.tiles[i]["IslandID"]):
                color = pygame.Color("white")
            else:
                color = pygame.Color("blue")

            pygame.draw.circle(self.surface, color,
                [xOffset + ei[0] * 32 + ei[1] * 32,
                yOffset - ei[0] * 56 + ei[1] * 56],
                31)

        for i in self.tiles:
            ei = eval(i)
            eiw = self.tiles[i]["Water horns"]
            if(eiw):
                self.surface.blit(textures.getImage('misc', '1horn'),
                [xOffset + ei[0] * 32 + ei[1] * 32,
                yOffset - ei[0] * 56 + ei[1] * 56 - 25])
        """


class Fleet:
    def __init__(self, surface, fleets, offset = [100,612]):
        self.surface = surface
        self.offset = [offset[0], offset[1]]
        self.timer = 0
        self.update(fleets)
    def update(self, fleets):
        self.fleets = fleets
        self.timer += 0.1
        if self.timer > 3.1:
            self.timer = -3.2
    def draw(self):
        xOffset = self.offset[0] + 10
        yOffset = self.offset[1]
        for i in self.fleets:
            ei = eval(i)
            playerID = self.fleets[i]["PlayerID"]
            shipsize = self.fleets[i]["Size"]

            if playerID == 1:
                shipcolor = "black"
            elif playerID == 2:
                shipcolor = "yellow"
            elif playerID == 3:
                shipcolor = "blue"
            elif playerID == 4:
                shipcolor = "red"
            elif playerID == 5:
                shipcolor = "green"
            else:
                shipcolor = "neutral"

            picname = "ship_{}_{}".format(shipcolor, shipsize)

            self.surface.blit(textures.getImage("ships", picname),
            [xOffset + ei[0] * 32 + ei[1] * 32 - 23,
            yOffset - ei[0] * 56 + ei[1] * 56 - 28])

class Island:
    def __init__(self, surface, islands, armies, offset = [100,612]):
        self.surface = surface
        self.offset = [offset[0], offset[1]]
        self.timer = 0
        self.update(islands, armies)
    def update(self, islands, armies):
        self.islands = islands
        self.armies = armies
    def draw(self):
        xOffset = self.offset[0] + 10
        yOffset = self.offset[1]
        for i in self.islands:
            playerID = self.islands[i]["Player"]

            if(playerID):
                if playerID == 1:
                    overlaycolor = "black"
                elif playerID == 2:
                    overlaycolor = "yellow"
                elif playerID == 3:
                    overlaycolor = "blue"
                elif playerID == 4:
                    overlaycolor = "red"
                elif playerID == 5:
                    overlaycolor = "green"

                overlay = "overlay_{}".format(overlaycolor)

                for ei in self.islands[i]["Tiles"]:
                    self.surface.blit(textures.getImage("maps", overlay),
                    [xOffset + ei[0] * 32 + ei[1] * 32 - 33,
                    yOffset - ei[0] * 56 + ei[1] * 56 - 33])

                for bi in range(len(self.islands[i]['Buildings'])):
                    b = self.islands[i]['Buildings'][bi]
                    #WIP


        for army in self.armies:
            islandID = eval(army)
            ei = averageCoords(self.islands[islandID]["Tiles"])

            self.surface.blit(textures.getImage("armies", "default_{}".format(self.armies[army]["Size"])),
            [xOffset + ei[0] * 32 + ei[1] * 32 - 33,
            yOffset - ei[0] * 56 + ei[1] * 56 - 33])



class Board:
    def __init__(self, screen, board, startcoords = [100,300], startsize = [500,500]):
        self.rect = pygame.Rect(startcoords[0], startcoords[1], startsize[0], startsize[1])
        self.screen = screen
        self.map = Map(screen, board["tiles"], [self.rect.x+312, self.rect.y+354])
        self.fleets = Fleet(screen, board["fleets"], [self.rect.x+312, self.rect.y+354])
        self.islands = Island(screen, board["islands"], board['armies'], [self.rect.x+312, self.rect.y+354])
    def update(self, board):
        self.map.update(board["tiles"])
        self.fleets.update(board["fleets"])
        self.islands.update(board["islands"], board['armies'])
    def draw(self):
        self.map.draw()
        self.fleets.draw()
        self.islands.draw()
        pygame.draw.rect(self.screen, pygame.Color("white"), self.rect, 2)
