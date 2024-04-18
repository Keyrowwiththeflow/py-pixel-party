import pygame
from pygame.locals import *

# We are making a ping pong game
class Player:
  def __init__(self, name: str, x_pos: int = 0, y_pos: int = 0, paddle_width: int = 0, paddle_height: int = 0, paddle_color: tuple = (0, 0, 0), speed: int = 1):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.paddle_width = paddle_width
    self.paddle_height = paddle_height
    self.paddle_color = paddle_color
    self.speed = speed

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

  # initialize the players
  player1 = Player("Player 1")
  player1.x_pos = 30
  player1.y_pos = 250
  player1.paddle_width = 15
  player1.paddle_height = 80
  player1.paddle_color = (255, 255, 255)
  player1.speed = 5
  
  player2 = Player("Player 2")
  player2.x_pos = 470
  player2.y_pos = 250
  player2.paddle_width = 15
  player2.paddle_height = 80
  player2.paddle_color = (255, 255, 255)
  player2.speed = 5

  # Game loop
  while running:
    # Capture input events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False

      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
        player1.y_pos -= player1.speed
      elif  keys[pygame.K_s]:
        player1.y_pos += player1.speed

    # Execute game logic
    
    # Update graphics
    window.fill((0,0,0))
    draw_paddle(player1, window)
    draw_paddle(player2, window)
    pygame.display.update()

  pygame.quit()

if __name__ == "__main__":
  main()