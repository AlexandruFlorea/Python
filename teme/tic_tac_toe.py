import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1

game = running
mark = 'X'


# game board
def draw_board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# Position check
def check_position(x):
    if board[x] == ' ':
        return True
    else:
        return False


# win check
def check_win():
    global game
    # Horizontal
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        game = win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        game = win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        game = win
    # Vertical
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        game = win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        game = win
    # Diagonal
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        game = win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        game = win
    # Match Tie or draw Condition
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        game = draw
    else:
        game = running


print("Welcome to a game of good old Tic-Tac-Toe")
print("Player 1 [X] --- Player 2 [O]")
print()
print("--- Game starting ---")
print("Please Wait...")

time.sleep(2)  # Pause, for dramatic effect

while game == running:
    draw_board()
    if player % 2 != 0:
        print("Your move, Player 1")
        mark = 'X'
    else:
        print("Your move, Player 2")
        mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark: "))

    if check_position(choice):
        board[choice] = mark
        player += 1
        check_win()


draw_board()

if game == draw:
    print("Tie!")
elif game == win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Wins!!!")
    else:
        print("Player 2 Wins!!!")
