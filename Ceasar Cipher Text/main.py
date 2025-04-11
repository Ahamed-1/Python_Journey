logo ='''
 _______                                 _______ _       _                 
(_______)                               (_______|_)     | |                
 _       _____ _____  ___ _____  ____    _       _ ____ | |__  _____  ____ 
| |     | ___ (____ |/___|____ |/ ___)  | |     | |  _ \|  _ \| ___ |/ ___)
| |_____| ____/ ___ |___ / ___ | |      | |_____| | |_| | | | | ____| |    
 \______)_____)_____(___/\_____|_|       \______)_|  __/|_| |_|_____)_|    
                                                  |_|                      
'''
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(direction,text,shift): 
        cipher_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the {direction}d result: {cipher_text}")

again = True

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)
    loop = input("Type 'yes' if you want to go again or type 'no':\n").lower()
    if loop == "no":
        again = False
    