"""Encontrar pares de palabras que formen palindromos en un diccionario
Para optimizar el tiempo, las listas han sido cambiadas por sets"""

import load_diccionary

word_list = load_diccionary.load('3of6game.txt')

def find_palingrams():
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

print("\nNumero de palindromos = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first,second))
