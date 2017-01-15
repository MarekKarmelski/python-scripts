#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Hangman game."""


from random import choice


def menu():
    """Game menu function."""
    print('Game menu:')
    print('1. Play game.')
    print('2. Exit game.')
    option = input('Choice the option [1-2]: ')
    option_number = 0
    if option.isdigit():
        option_number = int(option)
    return option_number


def hangman():
    """Hangman game function."""
    words = [
        'alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat',
        'cheetah', 'chicken', 'chimpanzee', 'cow', 'crocodile', 'deer',
        'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly',
        'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster',
        'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster',
        'monkey', 'octopus', 'owl', 'panda', 'pig', 'puppy', 'rabbit',
        'rat', 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake',
        'spider', 'squirrel', 'tiger', 'turtle', 'wolf', 'zebra'
    ]
    print('Category: ANIMALS')
    word_to_guess = choice(words).upper()
    mask_word_to_guess = []
    for letter in word_to_guess:
            mask_word_to_guess.append('_')
    guess = False
    game_round = 1
    while guess is not True:
        print('WORD TO GUESS: %s' % (' '.join(mask_word_to_guess)))
        print('Round: %s' % (game_round))
        user_word = input(
            'Type word or letter [exit - to stop game.]: ').upper()
        if user_word.lower() == 'exit':
            print('You lost!')
            print(
                'Word to guess was: %s, game rounds: %s' %
                (word_to_guess, game_round)
            )
            guess = True
        elif user_word == word_to_guess:
            print('You win!')
            print(
                'Word to guess was: %s, game rounds: %s' %
                (word_to_guess, game_round)
            )
            guess = True
        else:
            pos = 0
            for letter in word_to_guess:
                if letter == user_word:
                    mask_word_to_guess[pos] = letter
                pos += 1
            if ''.join(mask_word_to_guess) == word_to_guess:
                print('You win!')
                print(
                    'Word to guess was: %s, game rounds: %s' %
                    (word_to_guess, game_round)
                )
                guess = True
        game_round += 1
    return


def main():
    """Init hangman game function."""
    menu_options = [1, 2]
    print('HANGMAN GAME')
    play = True
    while play:
        option = menu()
        while option not in menu_options:
            print('Wrong option!')
            option = menu()
        if option == 1:
            hangman()
            play = False
        elif option == 2:
            play = False
            print('Exit game!.')
    return

main()
