
import pandas

data = pandas.read_csv("Pandas/24-NATO Alphabet Project/nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for index, row in data.iterrows()}
print(new_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
