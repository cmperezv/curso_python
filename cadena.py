#!/usr/bin/python
# -*- coding: utf-8 -*-

cadena = str(input("Escriba una palabra: "))
if cadena.isalnum():
    print("Consta de letras y/o números, sin espacios")
if cadena.isalpha():
    print("Consta de letras, sin números y sin espacios")
if cadena.isdigit():
    print("Consta sólo de números, sin espacios")

print("Texto en mayusculas: %s" % str(cadena.upper()))

print("Texto capitalizado: %s" % str(cadena.capitalize()))
