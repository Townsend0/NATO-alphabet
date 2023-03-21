import pandas
a = { b[1][0]: b[1][1] for b in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows() }
print( [ a[c] for c in input("Enter a word: ").upper() ] )