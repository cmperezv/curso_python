#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self, mamifero, perro, caniche):
        self.clasificacion = mamifero
        self.tipo = perro
        self.raza = caniche

    def __str__(self):
        return self.clasificacion + ": " + self.tipo + ", " + self.raza

class Perro(Animal):
    def __init__(self, mamifero, perro, caniche, cuatro):
        super(Perro, self).__init__(mamifero, perro, caniche)
        self.patas = cuatro

    def __str__(self):
        return self.clasificacion + ": " + self.tipo + ", " + self.raza + " (patas :" + self.patas + ")"


perro1 = Perro("mamifero", "perro", "caniche", "cuatro")
print(perro1)
