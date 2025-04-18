import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("300x200")

        # Buttons
        self.rock_btn = tk.Button(root, text="Rock", command=lambda: self.play("R"))
        self.rock_btn.pack(pady=5)

        self.paper_btn = tk.Button(root, text="Paper", command=lambda: self.play("P"))
        self.paper_btn.pack(pady=5)

        self.scissors_btn = tk.Button(root, text="Scissors", command=lambda: self.play("S"))
        self.scissors_btn.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def play(self, user_choice):
        choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
        computer_choice = random.choice(['R', 'P', 'S'])

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Update GUI
        self.result_label.config(
            text=f"Your choice: {choices[user_choice]}\n"
                 f"Computer's choice: {choices[computer_choice]}\n"
                 f"Result: {result}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
