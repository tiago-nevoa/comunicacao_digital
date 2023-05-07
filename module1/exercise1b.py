# coding=utf-8
#!/usr/bin/env python
import math
from pathlib import Path
import matplotlib.pyplot as plt

files_path = Path("TestFilesCD/")

# (b) Função que determina o máximo divisor comum entre dois números inteiros a e b, através do algoritmo de Euclides.
def sort(a, b):
    if a < b:
        aux = a
        a = b
        b = aux


def mdc(a, b):
    a = abs(a)
    b = abs(b)
    sort(a, b)
    remainder = a
    while remainder > 0:
        remainder = a % b
        a = b
        b = remainder
    return a

print("mdc =", mdc(92, -138))