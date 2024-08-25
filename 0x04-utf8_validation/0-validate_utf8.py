#!/usr/bin/python3
"""Utf8 string validation from integer list"""


def validUTF8(data):
    """Validate utf8 char"""
    for char in data:
        if char < 0 or char > 127:
            return False
    return True
