# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# import pandas
#
# code_words = pandas.read_csv('nato_phonetic_alphabet.csv')
# code_list = code_words.to_list()
# print(code_list)
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in code_words.iterrows():
    # Access index and row
    #  code_dict = {letter: code for (index, row) in code_words.iterrows()}
    # Access row.student or row.score
    # pass

# Keyword Method with iterrows()


import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
user_request = input('Enter a word: ').upper()
user_answer = [nato_dict[letter] for letter in user_request]
print(user_answer)