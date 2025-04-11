import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("\nWelcome to the secret auction program")
highest_bid = 0

shall_continue = True
bidders = {}
while shall_continue:
    name = input("What's your name? : ")
    bidders[name] = int(input("What's your bid? : $"))
    for name,bid in bidders.items():
        if bidders[name] > highest_bid:
            highest_bid = bid
            winner = name
    restart = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    os.system('cls')
    if  restart != "yes":
        shall_continue = False   
        print(f"The winner is {winner} with a bid of ${highest_bid}")

    