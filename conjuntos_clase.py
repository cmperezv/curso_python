#!/usr/bin/python
# -*- coding: utf-8 -*-

conjunto = "Carlos", "Pepe", "Maria", "Luisa"
alumnos = set(conjunto)
clase = set({"Carlos", "Pepe", "Maria", "Luisa", "Antonio", "Raul"})

clase.remove("Carlos")
clase.add("Manuel")

print("contenido actual del conjunto clase:")
for c in clase:
    print(c.ljust(15))

print("\n\nUnion de los dos conjuntos:")
for c in alumnos | clase:
    print(c.ljust(15))

print("\n\nIntersección de los dos conjuntos (elementos en común):")
for c in clase.intersection(alumnos):
    print(c.ljust(15))

print("\n\ndiferencia simétrica de los dos conjuntos (elementos que no están en ambos conjuntos):")
for c in clase.symmetric_difference(alumnos):
    print(c.ljust(15))
