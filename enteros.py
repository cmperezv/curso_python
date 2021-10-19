#!/usr/bin/python
# -*- coding: utf-8 -*-

def suma(operando1,operando2):
	return operando1 + operando2

def resta(operando1,operando2):
	return operando1 - operando2

def multiplica(operando1,operando2):
	return operando1 * operando2

def divide(operando1,operando2):
	if operando2 == 0 :
		return "No se puede dividir por cero"
	return operando1 / operando2


print(suma(5,7))
print(resta(5,7))
print(multiplica(5,7))
print(divide(5,7))
print(divide(5,0))
