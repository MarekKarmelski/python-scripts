#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Longest word function."""


def longest_word(text):
    """Longest word function."""
    list_of_words = text.split(' ')
    longest_word = ''
    longest_word_length = 0
    for word in list_of_words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word = word
    print(longest_word)

longest_word('ala ma kota a kot ma psa który mówi blablabla')
