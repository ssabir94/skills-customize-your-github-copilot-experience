# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python that practices strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from the provided `words` list and prepare the game state before asking the player to guess.

#### Requirements
Completed program should:

- Randomly select one word from the provided list.
- Track the letters the player has guessed and the number of incorrect guesses.
- Set a maximum of 6 incorrect guesses.
- Display each letter in the secret word as `_` until it has been guessed.

### 🛠️ Implement Guessing and Game Outcomes

#### Description
Run the game until the player guesses the word or uses all allowed incorrect guesses. Update and display the game state after each guess.

#### Requirements
Completed program should:

- Ask the player for one letter per turn and compare guesses without treating uppercase and lowercase letters differently.
- Reveal all matching positions when the guessed letter is in the secret word.
- Count an incorrect letter guess toward the 6-guess limit and show the remaining attempts.
- Continue displaying the word's progress and end when the word is fully revealed or the limit is reached.
- Display a clear win message for a correct completion, or a loss message that reveals the secret word.
