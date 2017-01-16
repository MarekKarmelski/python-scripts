#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Validate email using regular expression."""

import re


def validate_email(email_address):
    """Validate email function."""
    match = re.search(
        r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$',
        email_address
    )
    if match:
        return True
    else:
        return False

is_valid = validate_email('test@domain.com')
print(is_valid)
