import tkinter as tk
from tkinter import messagebox
import random

# ---------- Window ----------
root = tk.Tk()
root.title("Tic Tac Toe - Modern")
root.geometry("420x520")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# ---------- Variables ----------
human = "X"
ai = "O"
current_player = human
board = [""] * 9

player_score = 0
computer_score = 0

# ---------- Functions ----------
def check_winner():
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

def update_score():
    score_label.config(
        text=f"Player: {player_score}    Computer: {computer_score}"
    )

def ai_move():
    # Try to win
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            if check_winner() == ai:
                buttons[i].config(text=ai)
                return
            board[i] = ""

    # Try to block
    for i in range(9):
        if board[i] == "":
            board[i] = human
            if check_winner() == human:
                board[i] = ai
                buttons[i].config(text=ai)
                return
            board[i] = ""

    # Random move
    empty = [i for i in range(9) if board[i] == ""]
    move = random.choice(empty)
    board[move] = ai
    buttons[move].config(text=ai)

def check_game_end():
    global player_score, computer_score

    winner = check_winner()
    if winner == human:
        player_score += 1
        messagebox.showinfo("Result", "You Win!")
        reset_board()
    elif winner == ai:
        computer_score += 1
        messagebox.showinfo("Result", "Computer Wins!")
        reset_board()
    elif "" not in board:
        messagebox.showinfo("Result", "Draw!")
        reset_board()

    update_score()

def player_move(i):
    if board[i] == "":
        board[i] = human
        buttons[i].config(text=human)
        check_game_end()

        if "" in board and check_winner() is None:
            ai_move()
            check_game_end()

def reset_board():
    global board
    board = [""] * 9
    for b in buttons:
        b.config(text="")

def reset_scores():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    update_score()
    reset_board()

# ---------- UI ----------
title = tk.Label(
    root, text="TIC TAC TOE",
    font=("Segoe UI", 26, "bold"),
    fg="#f5c2e7", bg="#1e1e2e"
)
title.pack(pady=15)

score_label = tk.Label(
    root, text="Player: 0    Computer: 0",
    font=("Segoe UI", 14),
    fg="white", bg="#1e1e2e"
)
score_label.pack()

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=25)

buttons = []
for i in range(9):
    btn = tk.Button(
        frame, text="",
        font=("Segoe UI", 22, "bold"),
        width=5, height=2,
        bg="#313244", fg="white",
        activebackground="#585b70",
        command=lambda i=i: player_move(i)
    )
    btn.grid(row=i//3, column=i%3, padx=6, pady=6)
    buttons.append(btn)

tk.Button(
    root, text="Restart Board",
    font=("Segoe UI", 12),
    bg="#89b4fa", fg="black",
    command=reset_board
).pack(pady=5)

tk.Button(
    root, text="Reset Scores",
    font=("Segoe UI", 12),
    bg="#f38ba8", fg="black",
    command=reset_scores
).pack()

# ---------- Run ----------
root.mainloop()
