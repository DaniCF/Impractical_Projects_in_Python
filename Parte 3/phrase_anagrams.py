"""Crear un anagrama con el nombre y otras palabras elegidas por el usuario"""

import sys
from collections import Counter
import load_diccionary

dict_file = load_diccionary.load('3of6game.txt')

ini_name = input("Introduce un nombre: ")

def find_anagrams(name, word_list):
    """Lee el nombre y diccionario y muestra todos los anagramas EN el nombre"""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word)
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
            if Counter(test) == word_letter_map:
                anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print("Letras restantes = {}".format(name))
    print("Numero de letras restantes = {}".format(len(name)))
    print("Numero de anagramas (palabras reales) restantes = {}".format(len(anagrams)))

def process_choice(name):
    """Comprueba la eleccion del usuario por validez, devuelve eleccion y letras restantes."""
    while True:
        choice = input('\nEscoje una opcion. Sino pulsa Enter para volver a empezar o # para terminar: ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Eso no funciona! Haz otra eleccion!", file=sys.stderr)
    name = ''.join(left_over_list) #Hace que el display sea mas legible
    return choice, name

def main():
    """Ayuda al usuario a construir una frase anagrama con su nombre"""
    name = ''.join(ini_name.lower().split())
    name = name.replace('-','')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
            print("Longitud de la frase anagrama = {}".format(len(temp_phrase)))

            find_anagrams(name,dict_file)
            print("Anagrama actual = ", end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + " "
        
        elif len(temp_phrase) == limit:
            print("\n*****TERMINADO*****\n")
            print("Anagrama del nombre = ", end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\n\n¿Probar de nuevo? (Pulsa Enter, sino "n" para salir)\n ')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()