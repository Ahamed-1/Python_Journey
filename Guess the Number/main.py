import random
logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
'''

def check_answer(answer, guess): 
    if answer > guess:
        print("Too high")
    else:
        print("Too low")
    print("Guess Again")


def guess_number(chances):
    print (f"You have {chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return
    else:
        check_answer(guess,answer)

    chances -= 1
    if chances == 0:
        print(f"You've run out of guesses, you lose.The answer was {answer}")
        return
    
    guess_number(chances)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
answer = random.randint(1,100)

if level == 'easy':
    chances = 10
else:
    chances = 5

guess_number(chances)
    
