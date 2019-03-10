import pygame
from pygame.locals import *
import sys
import BackgroundTiles

class Main():
    mapWidth = 22
    mapHeight = 20


def main():
    screenSize= (Main.mapWidth*30, Main.mapHeight*30)
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Welcome to the game")
    pygame.display.update()

    GameMenu = True
    while(GameMenu):
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        for row in range(Main.mapHeight):
            for column in range(Main.mapWidth):
                pygame.draw.rect(screen, BackgroundTiles.Tiles.colors[BackgroundTiles.Tiles.tileMap[row][column]],(column*30, row*30, 30, 30))
        
        pygame.display.update()
            

        
    


if __name__ =="__main__":
    main()
    sys.exit()