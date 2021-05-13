"""Encontrar palindromos en una lista."""

import load_diccionary
import time

word_list = load_diccionary.load('3of6game.txt')
pali_list = []

start_time = time.time()
for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)
end_time = time.time()

print("\nNumero de palindromos encontrados = {}\n".format(len(pali_list)))
print(*pali_list,sep='\n')
print("Runtime del programa: {} segundos.".format(end_time - start_time))