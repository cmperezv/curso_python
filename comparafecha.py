#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

cadena = str(input("Escriba el anyo: "))
if cadena.isdigit():
	year1=cadena

cadena = str(input("Escriba el mes: "))
if cadena.isdigit():
	month1=cadena

cadena = str(input("Escriba el dia: "))
if cadena.isdigit():
	day1=cadena


print('Calculamos si la fecha introducida es mayor que la fecha de hoy:')

print('Fecha introducida:')
d1=datetime.date(int(year1),int(month1),int(day1))
print('\td1:', d1)

print('Fecha de hoy:')
d2 = datetime.date.today()
print('\td2:', d2)

print('\td1 > d2:', d1 > d2)
