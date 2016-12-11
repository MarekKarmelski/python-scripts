#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Guess the number."""

import random


def menu():
    """Game menu."""
    print('MENU:')
    print('1. Guess number from 1 to 100.')
    print('2. Guess number from 1 to 1000.')
    print('3. End game.')
    choice = input('Choice the option from 1 to 3: ')
    option_number = 0
    if choice.isdigit():
        option_number = int(choice)
    return option_number


def guess_number(flag=100):
    """Guess number function."""
    print('PC: Random number')
    number_to_guess = random.randint(1, flag)
    movements = 1
    find = False
    while (movements <= 5) and (find is not True):
        print('Movements: %s/5' % (movements))
        user_number = int(input('Tap your number: '))
        if user_number > number_to_guess:
            print('PC: My number is smaller.')
            movements += 1
        elif user_number < number_to_guess:
            print('PC: My number is bigger.')
            movements += 1
        else:
            print('You win! You guess the number! Number to guess was: %s' % (number_to_guess))
            find = True
    play_again = False
    if movements >= 5:
        print('You used up all the moves!')
    user_choice = input('Do You want play again? [Y - yes, n - not]: ')
    if user_choice.lower() == 'y':
        play_again = True
    else:
        print('Exit game!')
    return play_again


def main():
    """Init game function."""
    print('GUESS THE NUMBER')
    choices = [1, 2, 3]
    play = True
    while play:
        choice = menu()
        while choice not in choices:
            print('Wrong option!')
            choice = menu()
        if choice == 1:
            play_again = guess_number()
            if play_again is False:
                play = False
        elif choice == 2:
            play_again = guess_number(1000)
            if play_again is False:
                play = False
        elif choice == 3:
            play = False
            print('Exit game!.')
    return

main()
