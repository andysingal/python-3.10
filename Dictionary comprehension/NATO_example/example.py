import pandas as pd
from pprint import pprint

df = pd.read_csv('nato_phonetic_alphabet.csv')
print(len(df))

new_list = {row["letter"]: row["code"] for (index,row) in df.iterrows()}
print(new_list)

word = input("Enter a word: ").upper()
output_list = [new_list[letter] for letter in word]
print(output_list)



