"""Crea un 'grafico' contando las letras de una frase"""
import pprint

def main():
    phrase = input("Introduce una frase:\n").lower()
    char = 96

    for i in range(27):
        x = phrase.count(chr(char))
        print(chr(char) + ":" + (chr(char) * x))
        char = char + 1
    
if __name__ == '__main__':
    main()