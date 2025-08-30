import math

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")


def check_winner(board):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]
    for (x,y,z) in win_conditions:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    return None


def is_full(board):
    return " " not in board


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  
        return 1
    elif winner == "X":  
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:  
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:  
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe! You are X, AI is O")
    print_board(board)

    while True:
        
        move = int(input("Enter your move (0-8): "))
        if board[move] == " ":
            board[move] = "X"
        else:
            print("Invalid move, try again.")
            continue

        print_board(board)
        if check_winner(board) == "X":
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI plays:")
        print_board(board)

        if check_winner(board) == "O":
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

play_game()
