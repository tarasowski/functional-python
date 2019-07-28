# In Python 3, therea two types that represent sequences of characters: bytes and str
# Instances of bytes contain raw 8-bit values. Instances of str contain Unicode characters

import os


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Intance of str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else
        value = bytes_or_str
    return value # Instance of bytes

# The issue is that in Python 3, operations involving file handles (returned by the open built-in function) default to UTF-8 encoding. In Python 2, file operations default to binary endcoding.
# 'wb' means that the data is being opened in write binary mode instead of write character 'w'.
# This problem also exists for reading data from files. The solution is the same: Indicate binary mode by using 'rb' instead of 'r' when opening a file

with open ('./003-bytes-str.py', 'wb') as f:
    f.write(os.urandom(10))
