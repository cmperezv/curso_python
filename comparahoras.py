#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time

cadena = str(input("Escriba las horas: "))
if cadena.isdigit():
	hora1=cadena

cadena = str(input("Escriba los minutos: "))
if cadena.isdigit():
	minuto1=cadena


print('Calculamos si la hora introducida es mayor que la actual:')
t1 = datetime.time(int(hora1), int(minuto1), 0 )

print('\tt1:', t1)

hora_local = time.strftime("%H")
minutos_local = time.strftime("%M")

t2 = datetime.time(int(hora_local), int(minutos_local), 0 )

print('\tt2:', t2)
print('\tt1 > t2:', t1 > t2)
