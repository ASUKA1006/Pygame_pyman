import pygame
from pygame.locals import *
import sys
import BackgroundTiles


class Character(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.poo = pygame.image.load('res/'+filename)
        #for tilemap, scale(self.poo, 15, 15)
        self.small_poo = pygame.transform.scale(self.poo, (18, 18))

    def draw(self, screen, tile_x, tile_y):
        #for tilemap, blit(self.small_poo, (tile_x + 5,tile_y + 5))
        screen.blit(self.small_poo, (tile_x + 10,tile_y + 10))


def main():
    #for tilemap
    #mapWidth = 22
    #mapHeight = 21

    #for tilemap_easy
    mapWidth = 17
    mapHeight = 19

    screenSize= (mapWidth*45, mapHeight*45)
    screen = pygame.display.set_mode(screenSize)
    print(type(screen))
    pygame.display.set_caption("Welcome to the game")
    pygame.display.update()

    poo = Character('poo.png')

    GameMenu = True
    while(GameMenu):
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        for row in range(mapHeight):
            for column in range(mapWidth):
                tile_color = BackgroundTiles.Tiles.colors[BackgroundTiles.Tiles.tileMap_easy[row][column]]
                pygame.draw.rect(screen, tile_color,(column*45, row*45, 45, 45))
                if tile_color ==  BackgroundTiles.Tiles.BLACK:
                    tile_x = column * 45
                    tile_y = row * 45
                    poo.draw(screen, tile_x, tile_y)
                    
        #row_count =0
        #for row in BackgroundTiles.Tiles.tileMap:
            #for tile in row:
                #if tile == 1:
                    #tile_x = row.index(tile)
                    #tile_y = 
        
        pygame.display.update()
            


if __name__ =="__main__":
    main()
    sys.exit()