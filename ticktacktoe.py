# Tic Tac Toe game

# Tkinter liberary used for making gui apps using python
import tkinter as tk
from tkinter import messagebox


 # Function to check for winner
def check_winner():
    
 # Loop through all possible winning combinations
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# Function to handle button click
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Function to toggle current player
def toggle_player():
    global current_player
    current_player = "x" if current_player == "o" else "o"
    label.config(text=f"player {current_player}'s turn")

# Function to reset game
def reset_game():
    global current_player, winner
    current_player = "x"
    winner = False
    label.config(text=f"player {current_player}'s turn")
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

# Create main window
root = tk.Tk()
# Set title of main window
root.title("Tic Tac Toe")

buttons = [tk.Button(root,text="" , font = ("normal" , 25), width=6,height=2 , command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in grid layout
for i , button in enumerate(buttons):
    button.grid(row=i // 3 , column=i%3)

current_player = "x"
winner= False

# Create label to display current player's turn
label = tk.Label(root,text=f"player {current_player}'s turn",font=("normal",16))
label.grid(row=3,column=0,columnspan=3)

# Create reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start main event loop
root.mainloop()



