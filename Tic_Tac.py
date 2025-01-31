def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board, player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def play_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter positions (1-9) as shown below:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    while True:
        print_board(board)
        
        # Get valid input from current player
        while True:
            try:
                position = int(input(f"Player {current_player}, enter position (1-9): "))
                if 1 <= position <= 9:
                    if board[position-1] == ' ':
                        break
                    else:
                        print("That position is already taken!")
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Please enter a valid number!")
        
        # Update board
        board[position-1] = current_player
        
        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
            
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
            
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()