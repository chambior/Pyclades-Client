import pygame
import textures

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
        for i in self.tiles:
            ei = eval(i)
            pygame.draw.circle(self.surface, pygame.Color("white"),
                [xOffset + ei[0] * 32 + ei[1] * 32,
                yOffset + ei[0] * 56 - ei[1] * 56],
                33)
        for i in self.tiles:
            ei = eval(i)
            if(self.tiles[i]["IslandID"]):
                color = pygame.Color("green")
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


class Fleets:
    def __init__(self, surface, fleets, offset = [100,612]):
        self.surface = surface
        self.update(fleets)
        self.offset = [offset[0], offset[1]]
    def update(self, fleets):
        self.fleets = fleets
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
            [xOffset + ei[0] * 32 + ei[1] * 32 - 30,
            yOffset - ei[0] * 56 + ei[1] * 56 - 20])





class Board:
    def __init__(self, screen, board, startcoords = [100,300], startsize = [500,500]):
        self.rect = pygame.Rect(startcoords[0], startcoords[1], startsize[0], startsize[1])
        self.screen = screen
        self.map = Map(screen, board["tiles"], [self.rect.x+312, self.rect.y+354])
        self.fleets = Fleets(screen, board["fleets"], [self.rect.x+312, self.rect.y+354])
    def update(self, board):
        self.map.update(board["tiles"])
        self.fleets.update(board["fleets"])
    def draw(self):
        self.map.draw()
        self.fleets.draw()
        pygame.draw.rect(self.screen, pygame.Color("white"), self.rect, 2)
