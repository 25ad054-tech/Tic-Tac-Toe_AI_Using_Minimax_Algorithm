# Tic-Tac-Toe AI using Minimax Algorithm

import math

# Game board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

HUMAN = 'X'
AI = 'O'

# Print board
def print_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for winner
def check_winner(player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Check draw
def is_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Minimax algorithm
def minimax(depth, is_maximizing):
    if check_winner(AI):
        return 1
    if check_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = HUMAN
                    score = minimax(depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = AI

# Main game loop
def play_game():
    print("Tic-Tac-Toe AI")
    print("You are X, AI is O")

    while True:
        print_board()

        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = HUMAN

        if check_winner(HUMAN):
            print_board()
            print("🎉 You win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        # AI move
        best_move()

        if check_winner(AI):
            print_board()
            print("🤖 AI wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

# Run game
play_game()
