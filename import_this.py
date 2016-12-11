#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Import this."""


def printer_one():
    """Printer function."""
    zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of thos"""
    zen_list = zen.split('\n')
    del zen_list[0]
    for sentence in zen_list:
        index = sentence.find(',')
        if index > -1:
            print(sentence[index + 1:sentence.find('.')].strip())
    return

"""printer_one()"""


def printer_two():
    """Printer function."""
    zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of thos"""
    zen_list = zen.split('\n')
    s_len = len("\s") + 1
    del zen_list[0]
    for sentence in zen_list:
        index = sentence.find('is')
        if index > -1:
            print(sentence[index + s_len:sentence.find(' ', index + s_len)])
    return

"""printer_two()"""


def printer_three():
    """Printer function."""
    zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of thos"""
    zen_list = zen.split('\n')
    del zen_list[0]
    for sentence in zen_list:
        index = sentence.find('is')
        if index > -1:
            words = sentence[:index].split()
            if len(words) == 1:
                print(words[0])
            elif len(words) > 1:
                sentence_rev = ' '.join(reversed(words))
                print(sentence_rev[0:sentence_rev.find(' ')])
    return

"""printer_three()"""


def list_check():
    """Check list."""
    lista = list(range(0, 100))
    print(lista[::-1])
    print(lista[-65:-28])
    return

list_check()
