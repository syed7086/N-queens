import tkinter as tk

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))

def solve_and_display_n_queens(n, canvas):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n) is False:
        print("No solution exists")
    else:
        display_solution(board, canvas)

def display_solution(board, canvas):
    n = len(board)
    cell_size = 50
    canvas.config(width=n * cell_size, height=n * cell_size)

    for i in range(n):
        for j in range(n):
            x, y = j * cell_size, i * cell_size
            if board[i][j] == 1:
                canvas.create_text(x + cell_size // 2, y + cell_size // 2, text="Q", font=("Helvetica", cell_size // 2), fill="red")
            else:
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=color)

def display_n_queens_gui(n):
    window = tk.Tk()
    window.title("N-Queens Solver")

    canvas = tk.Canvas(window)
    canvas.pack()

    solve_and_display_n_queens(n, canvas)
    window.mainloop()
    
n = int(input("Enter Board size: "))

# n = 8  # Change this to the desired board size
display_n_queens_gui(n)
