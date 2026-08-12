import tkinter as tk
from tkinter import messagebox
import random

class CosmicGuessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cosmic Guess")
        self.root.configure(bg='#0a0a2a')

        # Game state
        self.secret_number = None
        self.attempts_left = 7
        self.game_active = False

        # Fonts
        self.title_font = ("Consolas", 48, "bold")
        self.label_font = ("Consolas", 20)
        self.button_font = ("Consolas", 16, "bold")
        self.feedback_font = ("Consolas", 18)

        self.setup_fullscreen()
        self.create_widgets()
        self.start_new_game()

    def setup_fullscreen(self):
        # Fullscreen setup
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.state('zoomed')
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def create_widgets(self):
        # Main layout
        main_frame = tk.Frame(self.root, bg='#0a0a2a')
        main_frame.pack(expand=True)

        # Title
        self.title_label = tk.Label(
            main_frame,
            text="Cosmic Guess",
            font=self.title_font,
            fg='#00ffff',
            bg='#0a0a2a'
        )
        self.title_label.pack(pady=50)

        # Instructions
        self.instruction_label = tk.Label(
            main_frame,
            text="Guess a number between 1 and 100. You have 7 attempts!",
            font=self.label_font,
            fg='#00cccc',
            bg='#0a0a2a'
        )
        self.instruction_label.pack(pady=20)

        # Input area
        input_frame = tk.Frame(main_frame, bg='#0a0a2a')
        input_frame.pack(pady=30)

        # Guess field
        self.guess_entry = tk.Entry(
            input_frame,
            font=self.label_font,
            width=10,
            justify='center',
            bg='#1a1a3a',
            fg='#ffffff',
            insertbackground='#00ffff',
            relief='solid',
            bd=2
        )
        self.guess_entry.pack(side=tk.LEFT, padx=10)
        self.guess_entry.bind('<Return>', lambda e: self.submit_guess())

        # Submit button
        self.submit_button = tk.Button(
            input_frame,
            text="Submit",
            font=self.button_font,
            bg='#00cccc',
            fg='#000000',
            activebackground='#00ffff',
            activeforeground='#000000',
            relief='raised',
            bd=3,
            command=self.submit_guess
        )
        self.submit_button.pack(side=tk.LEFT, padx=10)

        # Feedback text
        self.feedback_label = tk.Label(
            main_frame,
            text="",
            font=self.feedback_font,
            fg='#ffffff',
            bg='#0a0a2a',
            wraplength=600
        )
        self.feedback_label.pack(pady=20)

        # Attempts counter
        self.attempts_label = tk.Label(
            main_frame,
            text="Attempts left: 7",
            font=self.label_font,
            fg='#00ffff',
            bg='#0a0a2a'
        )
        self.attempts_label.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(
            main_frame,
            text="Restart Mission",
            font=self.button_font,
            bg='#ff00ff',
            fg='#ffffff',
            activebackground='#ff66ff',
            activeforeground='#000000',
            relief='raised',
            bd=4,
            command=self.start_new_game,
            height=2
        )
        self.restart_button.pack(pady=50)

    def start_new_game(self):
        # Reset game
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 7
        self.game_active = True
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.update_attempts_display()
        self.submit_button.config(state=tk.NORMAL)

    def submit_guess(self):
        # Process guess
        if not self.game_active:
            return

        try:
            guess_text = self.guess_entry.get().strip()
            if not guess_text:
                self.feedback_label.config(text="Enter a number!", fg='#ff6666')
                return
            guess = int(guess_text)
            if guess < 1 or guess > 100:
                self.feedback_label.config(text="Number must be between 1 and 100!", fg='#ff6666')
                return
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg='#ff6666')
            return

        self.attempts_left -= 1
        self.guess_entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.feedback_label.config(text="🚀 Congratulations! You guessed it!", fg='#00ff00')
            self.game_active = False
            self.submit_button.config(state=tk.DISABLED)
        elif self.attempts_left == 0:
            self.feedback_label.config(text=f"💥 Game over! The number was {self.secret_number}.", fg='#ff4444')
            self.game_active = False
            self.submit_button.config(state=tk.DISABLED)
        elif guess < self.secret_number:
            self.feedback_label.config(text="⬆️ Too low!", fg='#00ff88')
        else:
            self.feedback_label.config(text="⬇️ Too high!", fg='#ff8888')

        self.update_attempts_display()

    def update_attempts_display(self):
        # Update counter
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

    def run(self):
        # Start app
        self.root.mainloop()

if __name__ == "__main__":
    game = CosmicGuessGame()
    game.run()
