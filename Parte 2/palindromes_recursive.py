"""Encontrar palindromos en una lista.
Uso de metodo recursivo"""

import load_diccionary
import time

word_list = load_diccionary.load('3of6game.txt')
pali_list = []

def recursive(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] != word[len(word)-1]:
            return False
        else:
            word = word[1:-1]
            return recursive(word)

start_time = time.time()
for word in word_list:
    if recursive(word):
        pali_list.append(word)
end_time = time.time()

print("\nNumero de palindromos encontrados = {}\n".format(len(pali_list)))
print(*pali_list,sep='\n')

print("Runtime del programa: {} segundos.".format(end_time - start_time))