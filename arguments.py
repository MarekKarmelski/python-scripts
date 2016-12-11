#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Function arguments."""


def like(firstname, lastname, what='everything'):
    """Like function."""
    theme = '%s %s like %s.' % (firstname, lastname, what)
    print(theme)

like('Marek', 'Karmelski', what='sport')
