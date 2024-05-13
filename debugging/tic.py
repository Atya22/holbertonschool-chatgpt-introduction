#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
        board (list): The 3x3 board represented as a list of lists.
    """
    print("  0 | 1 | 2")  # Print column indices
    print("---------")
    for i, row in enumerate(board):
        print(i, "|".join(row))  # Print row index and row content
        print("---------")

def check_winner(board):
    """
    Checks if there is a winner on the Tic-Tac-Toe board.

    Args:
        board (list): The 3x3 board represented as a list of lists.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):  # Check rows for a winner
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:  # Check columns for a winner
            return True

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:  # Check diagonal from top-left to bottom-right
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:  # Check diagonal from top-right to bottom-left
        return True

    return False

def tic_tac_toe():
    """
    Plays a game of Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Start with player X
    print_board(board)  # Print the initial board
    while not check_winner(board):
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " " and 0 <= row <= 2 and 0 <= col <= 2:  # Check if the spot is available
                board[row][col] = player  # Place player's mark on the board
                if player == "X":
                    player = "O"  # Switch to player O
                else:
                    player = "X"  # Switch to player X
            else:
                print("Invalid input or spot already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter integers.")
        except IndexError:
            print("Invalid input! Row and column should be in range 0 to 2.")

    print_board(board)  # Print the final board
    print("Player " + player + " wins!")  # Print the winning player

if __name__ == "__main__":
    tic_tac_toe()  # Start the game


ard(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
        board (list): The 3x3 board represented as a list of lists.
    """
    print("  0 | 1 | 2")  # Print column indices
    print("---------")
    for i, row in enumerate(board):
        print(i, "|".join(row))  # Print row index and row content
        print("---------")

def check_winner(board):
    """
    Checks if there is a winner on the Tic-Tac-Toe board.

    Args:
        board (list): The 3x3 board represented as a list of lists.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):  # Check rows for a winner
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:  # Check columns for a winner
            return True

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:  # Check diagonal from top-left to bottom-right
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:  # Check diagonal from top-right to bottom-left
        return True

    return False

def tic_tac_toe():
    """
    Plays a game of Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Start with player X
    print_board(board)  # Print the initial board
    while not check_winner(board):
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " " and 0 <= row <= 2 and 0 <= col <= 2:  # Check if the spot is available
                board[row][col] = player  # Place player's mark on the board
                if player == "X":
                    player = "O"  # Switch to player O
                else:
                    player = "X"  # Switch to player X
            else:
                print("Invalid input or spot already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter integers.")
        except IndexError:
            print("Invalid input! Row and column should be in range 0 to 2.")

    print_board(board)  # Print the final board
    print("Player " + player + " wins!")  # Print the winning player

if __name__ == "__main__":
    tic_tac_toe()  # Start the game


import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) < 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
