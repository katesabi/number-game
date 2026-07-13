# 🎮 number guessing game

this  is a python script for a number guessing game. you have to guess a secret number between 1 and 100. the game tells you if your guess is too high, too low, or correct. you have 7 attempts.

## 🧠 what i learned

building this game helped me practice:  
- 👷 object‑oriented programming (oop) — structuring the game as a class with methods for initialization, ui creation, game logic, and event handling.  
- 🎨 tkinter gui development — creating an application with labels, buttons, entry fields, and dynamic feedback.  
- ⚡ event handling — binding keyboard events and button clicks to game functions.  
- ✅ input validation — checking user input for empty strings, non‑numeric values, and out‑of‑range numbers.  
- 📊 game state management — tracking attempts left, the secret number, and whether the game is active.  
- 🌈 visual design — using colors and fonts for a cohesive look.  
- 🤗 user experience (ux) — providing clear feedback, disabling buttons when the game ends, and offering a restart option.  

## ✨ features

- 🖥️ full‑screen mode with escape key to exit.  
- 💫 clean ui with custom colors and fonts.  
- ⌨️ input field that accepts guesses via enter key or the submit button.  
- 💬 real‑time feedback with color‑coded messages.  
- 🔢 attempts counter that updates after each guess.  
- 🔄 one‑click restart via the restart button at any time.  

## 🕹️ how to play

1. ▶️ run the `cosmic_guess.py` script in python.  
2. 🖼️ the game starts in full‑screen mode.  
3. 📖 read the instructions: guess a number between 1 and 100. you have 7 attempts.  
4. ✍️ type your guess in the input field and press enter or click the submit button.  
5. 🗣️ the game tells you:  
   - ⬇️ too low! if your guess is smaller than the secret number.  
   - ⬆️ too high! if your guess is larger than the secret number.  
   - 🎉 you guessed it! if you win.  
   - 😢 game over! the number was x. if you run out of attempts.  
6. 📉 the attempts left counter updates after every guess.  
7. 🔁 click restart to start a new game at any time.  

## ⚠️ known issues

- 🏃 the game does not prevent multiple guesses if the user spams the submit button very quickly.  
- ❓ unusual characters might cause minor display quirks.  
- 🌍 the full‑screen setup may behave slightly differently across operating systems.  

## 🚀 try it yourself

1. ⬇️ download the `cosmic_guess.py` file.  
2. 🐍 make sure you have python installed (3.6 or higher recommended).  
3. 💻 open a terminal or command prompt and navigate to the folder containing the script.  
4. ▶️ run the script:  
   ```bash
   python cosmic_guess.py

    <img width="1874" height="1042" alt="image" src="https://github.com/user-attachments/assets/9ea21f7f-74e1-466a-9279-aeb9d3be2c95" />

