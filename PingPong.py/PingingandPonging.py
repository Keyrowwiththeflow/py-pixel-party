import pygame
from pygame.locals import *

pygame.init()
#Screen size
screen_width = 500
screen_height = 500

running = True
#Game starting position
player1 = 1
player2 = -1
currentPlayer = player1
game_over = False

screen = pygame.display.set_mode = ((screen_width, screen_height))
pygame.display.set_caption = "Ping the Pong"
font = pygame.font.SysFont(None, 50)