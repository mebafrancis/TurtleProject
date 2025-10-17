import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_data)
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
#print(nato_dict)


user_input = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)