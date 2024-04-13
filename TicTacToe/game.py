import pygame 
from pygame.locals import *
import time

pygame.init()

# screen variables
screen_width = 300
screen_height = 300

# game state variables
running = True
markers = []

player1 = 1
player2 = -1
currentPlayer = player1

winner = 0
game_over = False

# UI variables for colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
beige = (255,255,200)
grey = (200,200,200)
line_color = (50,50,50)
line_width = 6

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TickTackToeBored")

font = pygame.font.SysFont(None, 40)

# Functions
def draw_grid():
  global screen

  bg = beige
  screen.fill(bg)
  for i in range(1,3):
    # draw vertical lines
    pygame.draw.line(screen, line_color, (100*i, 0), (100*i, screen_height), line_width) 

    #draw horizontal line
    pygame.draw.line(screen, line_color, (0, 100*i), (screen_width, 100*i), line_width)

def create_markers() -> list:
  board = []
  for i in range(3):
    row = [0] * 3
    board.append(row)
  
  return board 

def draw_x(x_pos, y_pos):
  global screen
  global red
  global line_width
  line_buffer = 15
  # draw a line from top left to lower right
  pygame.draw.line(screen, red, ((x_pos*100) + line_buffer, (y_pos*100) + line_buffer), ((x_pos*100) + (100 - line_buffer), (y_pos*100) + (100-line_buffer)), line_width)

  # draw a line from lower left to top right
  pygame.draw.line(screen, red, ((x_pos*100) + line_buffer, (y_pos*100) + (100 - line_buffer)), ((x_pos*100) + (100 - line_buffer), (y_pos*100) + line_buffer), line_width)

def draw_o(x_pos, y_pos):
  global screen
  global green
  global line_width
  line_buffer = 15

  pygame.draw.circle(screen, green, ((x_pos*100) + 50, (y_pos*100) + 50), 50 - line_buffer, line_width)


def draw_markers():
  x_pos = 0
  for x_row in markers:
    y_pos = 0
    
    for y_column in x_row:
      if y_column == player1:
        draw_x(x_pos, y_pos)
        # do stuff
      if y_column == player2:
        draw_o(x_pos, y_pos)

      y_pos += 1
    x_pos += 1    

def check_winner():
  global markers
  global winner
  global game_over

  for x_row in markers:
    # check the columns
    row_total = sum(x_row)
    if row_total == (player1 * 3):
      winner = 1
      game_over = True
      break
    if row_total == (player2 * 3):
      winner = 2
      game_over = True
      break
  
  # check the rows
  for y_pos in range(3):
    column_total = markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos]
    
    if column_total == (3 * player1):
      winner = 1
      game_over = True
      break
    
    if column_total == (3 * player2):
      winner = 2
      game_over = True
      break
   
  # check diagonals
    diag_total = markers[0][0] + markers[1][1] + markers [2][2]
    if diag_total == (3 * player1):
      winner = 1
      game_over = True
      break
    
    if diag_total == (3 * player2):
      winner = 2
      game_over = True
      break

    diag_total = markers[0][2] + markers[1][1] + markers [2][0]
    if diag_total == (3 * player1):
      winner = 1
      game_over = True
      break
    
    if diag_total == (3 * player2):
      winner = 2
      game_over = True
      break

def reset_board():
  global markers
  global winner
  global game_over
  global currentPlayer

  markers = []
  markers = create_markers()
  winner = 0
  game_over = False
  currentPlayer = player1

def display_winner():
  global winner
  global font

  winning_text = f"Player {winner} won!"
  winner_image = font.render(winning_text, True, blue)
  pygame.draw.rect(screen, grey, (screen_width//2 - 100, screen_height // 2 - 60, 200, 50))
  screen.blit(winner_image, (screen_width//2 - 90, screen_height//2 - 50))

markers = create_markers()

clicked = False

while running:
  draw_grid()
  draw_markers()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_r:
        reset_board()

    # capture mouse events in the window
    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
      clicked = True
    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
      clicked = False

      # determine where the mouse position is
      pos = pygame.mouse.get_pos()
      cell_x = pos[0]
      cell_y = pos[1]

      # map the mouse position to a cell by calculating the floor
      cell_x = cell_x // 100
      cell_y = cell_y // 100

      # check to see if the cell is occupied. If it is 0, it is not occupied by a player's marker
      if markers[cell_x][cell_y] == 0:
        markers[cell_x][cell_y] = currentPlayer
        currentPlayer *= -1
        check_winner()

  if game_over == True: 
    display_winner()

  pygame.display.update()      

pygame.quit()