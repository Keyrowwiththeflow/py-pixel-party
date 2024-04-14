import pygame 
from pygame.locals import *
from game_config import *

# Functions
def draw_grid(screen: pygame.Surface):
  bg = colors.beige
  screen.fill(bg)
  for i in range(1,3):
    # draw vertical lines
    pygame.draw.line(screen, colors.line_color, (100*i, 0), (100*i, game_settings.screen_height), game_settings.line_width) 

    #draw horizontal line
    pygame.draw.line(screen, colors.line_color, (0, 100*i), (game_settings.screen_width, 100*i), game_settings.line_width)

def create_markers() -> list:
  board = []
  for i in range(3):
    row = [0] * 3
    board.append(row)
  
  return board 

def draw_x(x_pos: int, y_pos: int, screen: pygame.Surface):
  # draw a line from top left to lower right
  pygame.draw.line(screen, colors.red, ((x_pos*100) + game_settings.line_buffer, (y_pos*100) + game_settings.line_buffer), ((x_pos*100) + (100 - game_settings.line_buffer), (y_pos*100) + (100-game_settings.line_buffer)), game_settings.line_width)

  # draw a line from lower left to top right
  pygame.draw.line(screen, colors.red, ((x_pos*100) + game_settings.line_buffer, (y_pos*100) + (100 - game_settings.line_buffer)), ((x_pos*100) + (100 - game_settings.line_buffer), (y_pos*100) + game_settings.line_buffer), game_settings.line_width)

def draw_o(x_pos: int, y_pos: int, screen: pygame.Surface):
  line_buffer = 15

  pygame.draw.circle(screen, colors.green, ((x_pos*100) + 50, (y_pos*100) + 50), 50 - line_buffer, game_settings.line_width)


def draw_markers(markers: list, screen: pygame.Surface):
  x_pos = 0
  for x_row in markers:
    y_pos = 0
    
    for y_column in x_row:
      if y_column == game_settings.player1:
        draw_x(x_pos, y_pos, screen)
        # do stuff
      if y_column == game_settings.player2:
        draw_o(x_pos, y_pos, screen)

      y_pos += 1
    x_pos += 1    

def check_winner(board) -> tuple[int, bool]: 
  winning_player = 0
  is_game_over = False

  for x_row in board:
    # check the columns
    row_total = sum(x_row)
    if row_total == (game_settings.player1 * 3):
      winning_player = 1
      is_game_over = True
      return winning_player, is_game_over
    if row_total == (game_settings.player2 * 3):
      winning_player = 2
      is_game_over = True
      return winning_player, is_game_over
  
  # check the rows
  for y_pos in range(3):
    column_total = board[0][y_pos] + board[1][y_pos] + board[2][y_pos]
    
    if column_total == (3 * game_settings.player1):
      winning_player = 1
      is_game_over = True
      return winning_player, is_game_over
    
    if column_total == (3 * game_settings.player2):
      winning_player = 2
      is_game_over = True
      return winning_player, is_game_over
   
  # check diagonals
  diag_total = board[0][0] + board[1][1] + board[2][2]
  if diag_total == (3 * game_settings.player1):
    winning_player = 1
    is_game_over = True
    return winning_player, is_game_over
  
  if diag_total == (3 * game_settings.player2):
    winning_player = 2
    is_game_over = True
    return winning_player, is_game_over

  diag_total = board[0][2] + board[1][1] + board[2][0]
  if diag_total == (3 * game_settings.player1):
    winning_player = 1
    is_game_over = True
    return winning_player, is_game_over
  
  if diag_total == (3 * game_settings.player2):
    winning_player = 2
    is_game_over = True
    return winning_player, is_game_over

  # finally check if there is a tie

  all_row_total = 0
  for x_row in board:
    all_row_total += sum(abs(entry) for entry in x_row)
 
  if (all_row_total == 9):
    winning_player = 0
    is_game_over = True
    return winning_player, is_game_over

  return 0, False


def display_winner(winning_player: int, font: pygame.font.Font, screen: pygame.Surface):

  if winning_player == 0:
    winning_text = "Nobody wins!"  
  else:
    winning_text = f"Player {winning_player} won!"
  
  winner_image = font.render(winning_text, True, colors.blue)
  pygame.draw.rect(screen, colors.grey, (game_settings.screen_width//2 - 100, game_settings.screen_height // 2 - 60, 200, 50))
  screen.blit(winner_image, (game_settings.screen_width//2 - 90, game_settings.screen_height//2 - 50))

def main():
 # game state variables
  currentPlayer = game_settings.player1
  running = True
  markers = []
  winner = 0
  game_over = False
  
  pygame.init()
  screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
  pygame.display.set_caption("TickTackToeBored")

  font = pygame.font.SysFont(None, 40)

  markers = create_markers()

  clicked = False

  while running:
    draw_grid(screen)
    draw_markers(markers, screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        if event.key == pygame.K_r:
          markers = []
          markers = create_markers()
          winner = 0
          game_over = False
          currentPlayer = game_settings.player1

      # capture mouse events in the window
      if game_over == False:
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
            results = check_winner(markers)
            game_over = results[1]
            if game_over:
              winner = results[0]

    if game_over == True: 
      display_winner(winner, font, screen)

    pygame.display.update()      

  pygame.quit()

if __name__ == "__main__":
  main()
