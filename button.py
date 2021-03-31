import pygame

pygame.init()

class Button:
    def __init__(self,
                    surface,
                    label='Bouton',
                    pos=[0,0],
                    size=[100,20],
                    color_default=pygame.Color("black"),
                    color_clicked=pygame.Color("dodgerblue2"),
                    font=pygame.font.Font(None, 16)
                    ):
        self.surface = surface
        self.label = label
        self.color_default = color_default
        self.color_clicked = color_clicked
        self.color = self.color_default
        self.font = font
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.label_surface = self.font.render(self.label, True, self.color)

    def handle_event(self, event, network):
        if(event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            if(self.color != self.color_clicked):
                board_g = eval(network.send("getBoard"))
                gods_g = eval(network.send("getGods"))
                auctions_g =  eval(network.send("getAuctions"))
            self.color = self.color_clicked
            return [True, board_g, gods_g, auctions_g]
        else:
            self.color = self.color_default
            return [False]


    def update(self):
        pass

    def draw(self):
        self.surface.blit(self.label_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.surface, self.color, self.rect, 2)
