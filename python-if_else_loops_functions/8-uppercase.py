#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(chr(ord(char) - 32) if 'a' <= char <= 'z' else char, end='')
    print()
