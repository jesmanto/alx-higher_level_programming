#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0] if len(sentence) > 0 else "None"
    tup = len(sentence), first_char
    return tup
