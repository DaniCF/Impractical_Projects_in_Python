"""Este programa genera permutaciones de 'tmvoordle' y las pasa a traves de filtros,
tipo 'Codigo de fuerza bruta Britanico', para encontrar palabras para un anagrama"""

import sys
from itertools import permutations
from collections import Counter
import load_diccionary

def main():
    """Cargar archivos, ejecutar filtros, permitir al usuario ver los anagramas por su primera letra."""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_diccionary.load('3of6game.txt')
    trigrams_filtered = load_diccionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """Preparar una lista de palabras para encontrar anagramas"""
    print("Longitud inicial word_list = {}".format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini if len(word) == len_name]
    print("length of new word_list = {}".format(len(word_list)))
    return word_list

def cv_map_words(word_list):
    """Mapea las letras de palabras en vocales y consonantes"""
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)
    #Determinar el numero de patrones c-v UNICOS
    total = len(set(cv_mapped_words))
    #Marcar una fraccion objetivo para eliminar
    target = 0.05
    #Conseguir el numero de objetos dentro de la fraccion objetivo
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print("Numero de filtered_cv_map = {}".format(len(filtered_cv_map)))
    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    """Borra permutaciones de palabras basandose en combinaciones consonante-vocal poco frecuentes"""
    perms = {''.join(i) for i in permutations(name)}
    print("Cantidad inicial del set de permutaciones = {}".format(len(perms)))
    vowels = 'aeiouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print("Numero de opciones despues de filter_1 = {}".format(len(filter_1)))
    return filter_1

def trigram_filter(filter_1, trigrams_filtered):
    """Borrar trios de letras poco comunes de las permutaciones."""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print("Numero de opciones despues de filter_2 = {}".format(len(filter_2)))
    return filter_2

def letter_pair_filter(filter_2):
    """Borrar pares de letras poco comunes de las permutaciones"""
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv','td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print("Numero de opciones despues de filter_3 = {}".format(len(filter_3)))
    if 'voldemort' in filter_3:
        print("¡Voldemort encontrado!", file=sys.stderr)
    return filter_3

def view_by_letter(name, filter_3):
    """Filtrar anagramas que empiecen por la letra introducida"""
    print("Letras restantes = {}".format(name))
    first = input("Selecciona una letra inicial o pulsa Enter para verlo todo: ")
    subset = [first]
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print("Numero de opciones que empiezan por {} = {}".format(first, len(subset)))
    try_again = input("¿Volver a probar? (Pulsa Enter sino cualquier tecla para salir):")
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()

if __name__ == '__main__':
    main()