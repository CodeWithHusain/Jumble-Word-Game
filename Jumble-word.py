import random


player1 = input("player1 Enter your name: " )
player2 = input("player2 Enter your name: " )
p1 = 0
p2 = 0
turn=0

words = [
    "apple", "brick", "chair", "dance", "eagle",
    "flame", "grape", "house", "ivory", "jelly",
    "knife", "lemon", "magic", "nurse", "ocean",
    "plant", "quest", "river", "stone", "tiger"
]



while True:
    selected_word=random.choice(words)


    
    jumbled_letters = list(selected_word) # this convert string into list becouse strings are unmutable
    random.shuffle(jumbled_letters) # it shuffle the word that are choosen
    jumbled_word = ''.join(jumbled_letters) # itsss join the word to look nice  

    print(jumbled_word)

    if(turn % 2==0):
        print(player1,"yours turn")
        guessed_word = input()
        if(guessed_word==selected_word):
            print("you won the price")
            p1 = p1+1 
        else:
            print(f"better luck next time the word was {selected_word}")

    else:
        print(player2,"your turn")
        guessed_word=input()     
        if(guessed_word==selected_word):
            print("you won the price")
            p2 = p2+1 
        else:
            print("better luck next time")
            print(f"better luck next time the word was {selected_word}")
    continue_game = input("Continue? (y/n): ")
    if continue_game.lower() != 'y':
        break

    turn += 1
print("\nFinal Scores:")
print(f"{player1}: {p1}")
print(f"{player2}: {p2}")

if p1 > p2:
    print(f"{player1} is the winner! 🏆")
elif p2 > p1:
    print(f"{player2} is the winner! 🏆")
else:
    print("It's a draw!")
