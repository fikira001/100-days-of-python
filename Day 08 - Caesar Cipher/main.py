# Define the alphabet list
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # Reverse shift for decoding
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char.lower() in alphabet:
            position = alphabet.index(char.lower())  # Get current index
            new_position = (position + shift_amount) % 26  # Shift and wrap
            new_char = alphabet[new_position]  # Get new letter
            
            # Maintain case (uppercase stays uppercase)
            if char.isupper():
                end_text += new_char.upper()
            else:
                end_text += new_char
        else:
            end_text += char  # Keep special characters unchanged

    print(f"Here's the {cipher_direction}d result: {end_text}")

# Loop to keep running the program
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # Ensure shift is within range

    # Call the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask if the user wants to continue
    restart = input("Type 'yes' to go again. Otherwise, type 'no':\n").strip().lower()
    if restart == "no":
        should_end = True
        print("Goodbye!")