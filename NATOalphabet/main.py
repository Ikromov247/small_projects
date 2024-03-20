import pandas as pd
import os

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

alphabet_csv = pd.read_csv(r"C:\Users\CheShire\PycharmProjects\NATOalphabet\nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
nato_alphabet = {row.letter: row.code for (index, row) in alphabet_csv.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user_input = input("Enter a name: ").strip().upper()
    if user_input.isalpha():
        nato_code = [nato_alphabet[letter] for letter in user_input]
        print(nato_code)
        break
    else:
        os.system("cls")
        print("Sorry, only letters in the alphabet")


