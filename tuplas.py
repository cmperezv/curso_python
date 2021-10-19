#!/usr/bin/python
# -*- coding: utf-8 -*-

alumnos = "Carlos", "Maria", "Juan"
apellidos = "Gonzalez", "Perez", "Rodriguez"
notas = 9, 7, 5

for al, ap, no in zip(alumnos, apellidos, notas):
    print("%s %s: %d." % (al, ap, no))
