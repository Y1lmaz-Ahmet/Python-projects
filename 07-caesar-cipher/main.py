alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_input,shift_amount,direction):
  output_text = ""
  if direction == "decode":
    shift_amount *= -1
  for letter in text_input:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    output_text += alphabet[new_position]
  print(f"The {direction} text is {output_text}")
  
caesar(text_input=text, shift_amount=shift,direction=direction)