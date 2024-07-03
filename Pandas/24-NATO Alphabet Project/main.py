
import pandas

data = pandas.read_csv("24-NATO Alphaet Project/nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for index, row in data.iterrows()}

# print(new_dict)

word = input("Enter a word: ").upper()

output_list = [new_dict[letter] for letter in word]

print(output_list)

