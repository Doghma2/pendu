# -*- encoding: utf-8 -*-

import random

def convert_txt(path):
    """Fonction to get all word from our txt file and return it
    as a list of items"""
    with open(path, 'r', encoding='utf8') as File:
        content = File.read().split('\n')

        return content




def game_loop(WORD):
    print(WORD)
    pass



def main():
    #Get all of our word as a list
    WORDS_SET = convert_txt("littre.txt")

    #Launch a game with a random word
    game_loop(random.choice(WORDS_SET))

if __name__ == '__main__':
    main()
