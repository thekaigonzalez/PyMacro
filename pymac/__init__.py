import os

from pymac.pyMacParse import Lexer

def PyMacInit(code):
    tokens = Lexer(code)
    return tokens