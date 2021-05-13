"""Encontrar los anagramas de una palabra introducida por el usuario"""
import load_diccionary

word_list = load_diccionary.load('3of6game.txt')

anagram_list = []

name = 'Daniel'
print("Nombre input = {}".format(name))
name = name.lower()
print("Nombre en uso = {}".format(name))

name_sorted = sorted(name)
for word in word_list:
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

print()
if len(anagram_list) == 0:
    print("Necesitas un nuevo diccionario u otro nombre")
else:
    print("Anagramas =", *anagram_list, sep='\n')