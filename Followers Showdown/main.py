from game_data import data
from art import logo,vs
import random
import os

def select():
    return random.choice(data)

def print_details(alphabet, person):
    print(f"Compare {alphabet}: {person['name']}, {person['description']}, from {person['country']}")

def compare(person_1, person_2):
    result = person_1['follower_count'] > person_2['follower_count']
    return result

def clean():
    os.system('cls')
    print(logo)

def higher_or_lower(celebrity_1, score):
    clean()
    if score > 0:
        print(f"You're right! Current score: {score}.")
    celebrity_2 = select()
    while celebrity_1 == celebrity_2:
        celebrity_2 = select()

    print_details("A", celebrity_1)
    print(vs)
    print_details("B", celebrity_2)

    user_choice = input(f"Who has more followers? Type 'A' or 'B':").upper()
    answer = compare(celebrity_1, celebrity_2)
    if (user_choice == 'A' and answer == True) or (user_choice == 'B' and answer == False) :
        score += 1
        celebrity_1 = celebrity_2
    else:
        clean()
        print(f"Sorry, that's wrong. Final score:{score}")
        return
    
    
    

    higher_or_lower(celebrity_1, score)

celebrity_1 = select()
score = 0
higher_or_lower(celebrity_1,score)
