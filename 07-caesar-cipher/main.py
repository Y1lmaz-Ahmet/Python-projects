alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_input,shift_amount,direction):
  output_text = ""
  for char in text_input:
    position = alphabet.index(char)
    if direction == "encode":
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      output_text += new_letter
    elif direction == "decode":
      new_position = position - shift_amount
      new_letter = alphabet[new_position]
      output_text += new_letter
  print(f"The {direction} text is {output_text}")


    

caesar(text_input=text, shift_amount=shift,direction=direction)