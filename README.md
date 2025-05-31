# 🧩 Two-Player Jumbled Word Guessing Game

A simple interactive Python game where two players take turns guessing a shuffled (jumbled) word. Points are awarded for correct guesses, and the player with the highest score at the end wins!

---

## 🎯 Game Objective

Guess the correctly spelled word from a scrambled (jumbled) version presented by the program. Players alternate turns trying to guess the word. The game continues until players decide to stop.

---

## 🕹️ How to Play

1. Run the script.
2. Enter Player 1 and Player 2 names.
3. On each turn, a jumbled word is shown.
4. The current player tries to guess the original word.
5. If the guess is correct, the player earns a point.
6. Players choose to continue or stop after each round.
7. Scores are displayed at the end, and the winner is announced.

---

## ⚙️ How It Works

- A list of words is predefined.
- The program randomly selects a word each round.
- The word is jumbled by shuffling its letters.
- Players take turns guessing the original word.
- The program tracks scores for both players.
- The game loops until players decide to quit.

---

## 🚀 Running the Game

Save the script as `jumbled_word_game.py` and run it using Python 3:

```bash
python jumbled_word_game.py
player1 Enter your name: Alice
player2 Enter your name: Bob

pplae
Alice yours turn
apple
you won the price

Continue? (y/n): y

grape
Bob your turn
graph
better luck next time the word was grape

Continue? (y/n): n

Final Scores:
Alice: 1
Bob: 0
Alice is the winner! 🏆
