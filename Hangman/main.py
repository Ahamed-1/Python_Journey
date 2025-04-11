#Day 6 project is to tackle the maze in reboorg's world. Reboorg is a cute little robot that lives in a maze.
import random
from hangman_art import stages, hangman
from hangman_words import words

print(hangman)


chosen_word = random.choice(words)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
display_list = []
for position in range(word_length):
  placeholder+= "_"
  display_list.append("_")
print("Word to Guess " + placeholder)

display = ""

game_over = False
lives = 6

while not game_over:
    print(f"******************************{lives}/6 LIVES LEFT******************************")
    
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display_list:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        print(f"You guessed {guess} that's in the word. Great go ahead")
        

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that's not in the word. You lose a life")
    
    for index in range(word_length):
        if chosen_word[index]  == guess:
            display_list[index] = guess

    display = "".join(map(str,display_list))
    print(display)
    if "_" not in display:
        game_over = True
        print("******************************YOU WIN******************************")
    elif lives == 0:
        game_over = True
        print(f"******************************IT WAS {chosen_word}.YOU LOSE******************************")
    
    print(stages[lives])
    

    