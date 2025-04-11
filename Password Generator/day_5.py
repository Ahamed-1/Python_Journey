import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for i in range(no_of_letters):
    password_list.append(random.choice(letters))

for j in range(no_of_numbers):
    # password_list.insert(random.randint(0,len(passwor_list)-1),random.choice(numbers))
    password_list.append(random.choice(numbers))

for k in range(no_of_symbols):
    # password_list.insert(random.randint(0,len(password_lidst)-1),random.choice(symbols))
    password_list += random.choice(symbols)


random.shuffle(password_list)

# final_password = ""
# for char in password_list:
#     final_password += char

final_password = ''.join(map(str,password_list))

print(f"Here is your password: {final_password}")