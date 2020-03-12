# global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_still_going = True
winner = None
current_player = "X"

# the function below is the step by step execution of all the functions defined below.
def play_game():
  print("\n    X - O     G A M E\n")
  print("Note : Use the numpad to enter X or O in respective fields.\n")
  display_board()
  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner == "X" or winner == "O":
    print("PLAYER",winner,"IS THE WINNER !!.")
  elif winner == None:
    print("Tie.")
  print("\nT H A N K S     F O R     P L A Y I N G     ! ! ! ! !")

# shows the game board with the help of the list named 'board'(line 2) 
def display_board():
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9\n")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3\n")

# manages the turn of single player at a time
def handle_turn(player):
  print("Player",player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  board[position] = player
  display_board()

# verifies if the game is completed
def check_if_game_over():
  check_for_winner()
  check_for_tie()

def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None

def check_columns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None

def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None

def check_for_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

# call the function
play_game()
