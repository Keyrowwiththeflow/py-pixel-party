import pygame
from pygame.locals import *

# We are making a ping pong game
class Player:
  def __init__(self, name: str):
    self.name = name

  def __init__(self, name: str, x_pos: int, y_pos: int, paddle_width: int, paddle_height: int, paddle_color: tuple):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.paddle_width = paddle_width
    self.paddle_height = paddle_height
    self.paddle_color = paddle_color

player1 = Player("Player 1", 100, 250, 25, 50, (255, 255, 255))
player2 = Player("Player 2", 400, 250, 25, 50, (255, 255, 255))


def draw_paddle(player: Player, screen: pygame.Surface):
  pygame.draw.rect(screen, player.paddle_color, (player.x_pos, player.y_pos, player.paddle_width, player.paddle_height))

def main():
  pygame.init()
  #Screen size
  screen_width = 500
  screen_height = 500

  running = True
  #Game starting position
  
  game_over = False

  window = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Ping the Pong")
  font = pygame.font.SysFont(None, 50)

  # Game loop
  while running:
    # Capture input events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # Execute game logic
    
    # Update graphics
    draw_paddle(player1, window)
    pygame.display.update()

  pygame.quit()

if __name__ == "__main__":
  main()