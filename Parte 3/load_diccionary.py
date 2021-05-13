"""Cargar un archivo de texto como una lista de strings en minuscula."""

import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError al abrir {}. Terminando programa.".format(e,file),file=sys.stderr)
        sys.exit(1)