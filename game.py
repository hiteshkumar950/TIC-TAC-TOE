import tkinter as tk
from tkinter import messagebox

# Function to check the winner
def check_winner():
    # Check rows
    for i in range(rows):
        if all(board[i][j] == board[i][0] and board[i][j] != "" for j in range(cols)):
            return board[i][0]
    
    # Check columns
    for j in range(cols):
        if all(board[i][j] == board[0][j] and board[i][j] != "" for i in range(rows)):
            return board[0][j]
    
    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != "" for i in range(min(rows, cols))):
        return board[0][0]
    
    if all(board[i][cols-1-i] == board[0][cols-1] and board[i][cols-1-i] != "" for i in range(min(rows, cols))):
        return board[0][cols-1]
    
    return None

# Function to handle the player's move
def player_move(row, col):
    if board[row][col] == "":
        board[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get(), fg=player_colors[current_player.get()])
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j] != "" for i in range(rows) for j in range(cols)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player.set("O" if current_player.get() == "X" else "X")

# Function to reset the game
def reset_game():
    global board
    board = [["" for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            buttons[i][j].config(text="", fg="black")

# Function to create the grid dynamically based on user input
def create_game_grid():
    global rows, cols, buttons, board, current_player
    rows = int(entry_rows.get())
    cols = int(entry_cols.get())
    
    # Initialize the game state and current player
    current_player = tk.StringVar(value="X")
    board = [["" for _ in range(cols)] for _ in range(rows)]
    
    # Set up the buttons
    buttons = [[tk.Button(window, text="", width=10, height=3, font=("Arial", 20),
                          command=lambda row=i, col=j: player_move(row, col))
                for j in range(cols)] for i in range(rows)]

    # Grid layout for the buttons
    for i in range(rows):
        for j in range(cols):
            buttons[i][j].grid(row=i, column=j)

# Set up the window
window = tk.Tk()
window.title("Tic Tac Toe")

# Define colors for X and O
player_colors = {"X": "green", "O": "orange"}

# Ask for user input for rows and columns
label_rows = tk.Label(window, text="Enter number of rows:")
label_rows.grid(row=0, column=0)
entry_rows = tk.Entry(window)
entry_rows.grid(row=0, column=1)

label_cols = tk.Label(window, text="Enter number of columns:")
label_cols.grid(row=1, column=0)
entry_cols = tk.Entry(window)
entry_cols.grid(row=1, column=1)

# Button to start the game
start_button = tk.Button(window, text="Start Game", command=create_game_grid)
start_button.grid(row=2, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
