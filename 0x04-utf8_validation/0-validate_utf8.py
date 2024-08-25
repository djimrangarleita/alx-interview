"""Utf8 string validation from integer list"""
#!/usr/bin/python3


def validUTF8(data):
    for char in data:
        if char < 0 or char > 127:
            return False
    return True
